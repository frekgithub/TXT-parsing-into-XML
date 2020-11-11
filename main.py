with open("test.txt", "r") as f:  # 打开文件
    import xml.etree.cElementTree as ET

    root = ET.Element("Tags",locale="zh_CN",MinVersion="8.0.0")
    root1 = ET.SubElement(root, "Tag",type="Folder",name="FiratNew Folder")
    doc = ET.SubElement(root1, "Tags")

    data = f.readlines()  # 读取文件
    i=0
    for tt in data:
        if i==0:
            str=(tt.lstrip()).split( )
            print(str[1],str[2])
            astr=str[1]
            #print(astr)
            a1str =(astr.lstrip()).split('=')
            a2str=(a1str[3])
            a3str=a1str[3].replace('"','')
            #print(a3str)

            bstr = str[2]
            b1str = (bstr.lstrip()).split(':')
            b2str = (b1str[1])
            b3str = b1str[1].replace('"', '')
            #print(b3str)

            cstr = str[3]
            # print(cstr)
            c1str = (cstr.lstrip()).split('=')
            c2str = (c1str[1])
            c3str = c1str[1].replace('"', '')
            # print(c3str)
            if c3str=="INT":
                aaa="2"
            elif c3str=="BOOL":
                aaa="7"
            elif c3str=="REAL":
                aaa="5"
            else:
                aaa="2"
            # print(aaa)
            doc1 = ET.SubElement(doc, "Tag",type="AtomicTag",name=b3str)
            ET.SubElement(doc1, "Property", name="valueSource").text = "opc"
            ET.SubElement(doc1, "Property", name="opcItemPath").text = "ns=2;s="+a3str
            ET.SubElement(doc1, "Property", name="dataType").text =aaa
            ET.SubElement(doc1, "Property", name="opcServer").text = "Ignition OPC UA Server"
        i = i + 1
        if i==11:
            i=0
    tree = ET.ElementTree(root)
    tree.write("newTag.xml")
    print("生成成功")