import re
import os

def remove_comments_from_file(filename):
    
    with open(filename, 'r') as file:
        code = file.read()
    
   
    code = re.sub(r'#.*', '', code)
  
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
    
 
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}-no-comments{ext}"
    
   
    with open(new_filename, 'w') as file:
        file.write(code)

    print(f"Comments removed. The file has been saved as {new_filename}")


filename = 'example.py'  
remove_comments_from_file("scraper2.py")
