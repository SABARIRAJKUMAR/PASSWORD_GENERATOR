words=["a","d","r","e"]
files=open("password1.txt","a")
for i in words:
    for j in words:
        for k in words:
            for l in words:
                files.write(f"{i}{j}{k}{l}\n")
files.close()
#Code with ❤️ by SABARIRAJKUMAR
