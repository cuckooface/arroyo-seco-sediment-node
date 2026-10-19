import PDFKit
import AppKit
let args = CommandLine.arguments
let doc = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let out = args[2]
for i in 0..<doc.pageCount {
  let p = doc.page(at: i)!
  let b = p.bounds(for: .mediaBox)
  let scale = 1600.0 / max(b.width, b.height)
  let img = p.thumbnail(of: NSSize(width: b.width*scale, height: b.height*scale), for: .mediaBox)
  let rep = NSBitmapImageRep(data: img.tiffRepresentation!)!
  try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "\(out)/p\(String(format:"%02d", i+1)).png"))
}
print(doc.pageCount)
