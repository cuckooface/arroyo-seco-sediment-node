import Foundation
import CoreGraphics
// usage: comp overall.pdf building.pdf out.pdf k dx dy  eraseX0 eraseX1 eraseY0 eraseY1  clipX0 clipX1 clipY0 clipY1   (erase/clip in top-down image coords of overall page)
let a = CommandLine.arguments
let os = CGPDFDocument(URL(fileURLWithPath: a[1]) as CFURL)!.page(at: 1)!
let bs = CGPDFDocument(URL(fileURLWithPath: a[2]) as CFURL)!.page(at: 1)!
var box = os.getBoxRect(.mediaBox); let H = box.height
let v = a[4...].map { Double($0)! }
let k = v[0], dx = v[1], dy = v[2]
func r(_ x0: Double, _ x1: Double, _ y0: Double, _ y1: Double) -> CGRect { CGRect(x: x0, y: Double(H) - y1, width: x1 - x0, height: y1 - y0) }
let ctx = CGContext(URL(fileURLWithPath: a[3]) as CFURL, mediaBox: &box, nil)!
ctx.beginPDFPage(nil)
ctx.drawPDFPage(os)
ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1)); ctx.fill(r(v[3], v[4], v[5], v[6]))
ctx.saveGState()
ctx.clip(to: r(v[7], v[8], v[9], v[10]))
ctx.setBlendMode(.multiply)
ctx.concatenate(CGAffineTransform(a: k, b: 0, c: 0, d: k, tx: dx, ty: dy))
ctx.drawPDFPage(bs)
ctx.restoreGState()
ctx.endPDFPage(); ctx.closePDF()
print("ok")
