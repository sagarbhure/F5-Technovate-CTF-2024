from PyPDF2 import PdfWriter, PdfReader

output = PdfWriter()
reader = PdfReader(open('original.pdf', 'rb'))

for i in range(len(reader.pages)):
	page = reader.pages[i]
	output.add_page(page)

with open('out.pdf', 'wb') as f:
    output.add_js("var _0d490b = ['281588gjHyaC', '118851wGAlqt', '1145119HHsRSD', '524842LzeAHf', '83nxJgRv', '285069HCsKvc', '889UqMaIT', '1DXgMVR', '144677lUYHdN'];var _0n907b = function(_0x294226, _0x4a3243) { _0x294226 = _0x294226 - 0x136; var _0d490b45 = _0d490b[_0x294226]; return _0d490b45;};(function(_0x1a3463, _0x59bc93) { var _0x230651 = _0n907b; while (!![]) { try { var _0x1470d5 = -parseInt(_0x230651(0x13b)) + -parseInt(_0x230651(0x13e)) * parseInt(_0x230651(0x137)) + parseInt(_0x230651(0x136)) + -parseInt(_0x230651(0x13d)) + -parseInt(_0x230651(0x139)) + -parseInt(_0x230651(0x13a)) + -parseInt(_0x230651(0x13c)) * -parseInt(_0x230651(0x138)); if (_0x1470d5 === _0x59bc93) break; else _0x1a3463['push'](_0x1a3463['shift']()); } catch (_0x56827b) { _0x1a3463['push'](_0x1a3463['shift']()); } }}(_0d490b, 0x45eeb), console['l' + 'o' + 'g']('t' + 'e' + 'c' + 'h' + 'n' + 'o' + 'v' + 'a' + 't' + 'e' + '{' + 'e' + 'm' + '2' + 'E' + '4' + 'e' + '4' + '_' + 'p' + 'd' + 'f' + '$' + '$' + '2' + '0' + 'x' + '1' + '4' + '7' + '0' + 'd' + '5' + '}'));")
    output.write(f)
