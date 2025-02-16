from data.containers import vector

class fstream():
    def fin(filename):
        return open(filename, "r")

    def fout(filename):
        return open(filename, "w")
    
    def fread(filename):
        with open(f"{filename}", "r") as f:
            return f.read()
        
    def fread_as_vec(filename):
        with open(f"{filename}", "r") as f:
            return (f.readlines())
    
    def fwrite(filename, content):
        with open(f"{filename}", "w") as f:
            f.write(content)

    def can_write(filename):
        with open(f"{filename}", "w") as f:
            return filename.writable()
    
    def fwrite_as_vec(filename, content):
        if not isinstance(content, vector):
            raise TypeError(f"fstream.fwrite_as_vec({filename}, {content}) only takes <vector> argument, not {type(content)}")
        with open(f"{filename}", "w") as f:
            f.writelines(content._data)

    def can_read(filename):
        with open(f"{filename}", "r") as f:
            return f.readable()