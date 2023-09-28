import os
f = input("Enter a filename: ")
base, extension = os.path.splitext(f)
extension_ = {
    '.txt': 'Text Document',
    '.doc': 'Word Document',
    '.pdf': 'PDF Document',
    '.jpg': 'JPEG Image',
    '.png': 'PNG Image',
    '.xlsx': 'Excel Spreadsheet',
    '.py':'Python file',
    
}
full_form = extension_.get(extension.lower(), 'Unknown File Type')
print(f"The full form of the file extension {extension} is: {full_form}")
