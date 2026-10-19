import Foundation
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers
// usage: trim in.pdf out.png longEdgePx
let a = CommandLine.arguments
let doc = CGPDFDocument(URL(fileURLWithPath: a[1]) as CFURL)!
let page = doc.page(at: 1)!
let box = page.getBoxRect(.mediaBox)
let s = Double(a[3])! / Double(max(box.width, box.height))
let w = Int(box.width * s), h = Int(box.height * s)
let cs = CGColorSpaceCreateDeviceRGB()
let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: w*4, space: cs, bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1)); ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
ctx.interpolationQuality = .high
ctx.scaleBy(x: s, y: s); ctx.translateBy(x: -box.minX, y: -box.minY)
ctx.drawPDFPage(page)
let data = ctx.data!.bindMemory(to: UInt8.self, capacity: w*h*4)
var x0 = w, y0 = h, x1 = 0, y1 = 0
for y in 0..<h { for x in 0..<w { let i = (y*w + x)*4
  if data[i] < 235 || data[i+1] < 235 || data[i+2] < 235 { if x < x0 {x0 = x}; if x > x1 {x1 = x}; if y < y0 {y0 = y}; if y > y1 {y1 = y} } } }
let pad = Int(Double(max(w,h)) * 0.01)
x0 = max(0, x0-pad); y0 = max(0, y0-pad); x1 = min(w-1, x1+pad); y1 = min(h-1, y1+pad)
let img = ctx.makeImage()!.cropping(to: CGRect(x: x0, y: y0, width: x1-x0+1, height: y1-y0+1))!
let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[2]) as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, img, nil); CGImageDestinationFinalize(dest)
print(a[2].split(separator: "/").last!, img.width, "x", img.height)
