print("<!DOCTYPE>")
print("<html>")
print("<head>")
print("</head>")
print("<body>")
print("<table>")
for i in range(1, 10):
    print(f"<tr>")
    for j in range(1, 10):
        print(f"<td>{i*j}</td>")
    print(f"</tr>")
    print()
print("</table>")
print("</body>")
print("</html>")