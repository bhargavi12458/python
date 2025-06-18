try:
    file=open("my file.txt","r")
    except IOerror:
        print("error:unable to read the file!")
        finally:
            file.close()
            
