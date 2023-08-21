#   Made By Leviathenn  #

import os
import subprocess
import time

def compile_files(src_dir, build_dir, include_dir):
    print("(!) JIT Build Created By Leviathenn")
    print("(-) Compiling...")
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".c") or file.endswith(".h") or file.endswith(".hpp"):

                
                subdir_name = os.path.relpath(root, src_dir)
                print("(-) Compiling: "+root+"\\"+file);
                obj_name = os.path.splitext(file)[0]
                target_obj_path = os.path.join(build_dir, subdir_name+".o")
                
                os.makedirs(os.path.dirname(target_obj_path), exist_ok=True)
                
                compile_command = [
                    "g++", "-std=c++11", "-Wall",
                    "-c", os.path.join(root, file),
                    "-o", target_obj_path,
                    "-I", include_dir,
                    "-lstdc++"
                ]
                subprocess.run(compile_command)

                print("(!) Compiled "+root+"\\"+file);
                time.sleep(2);
                
                print("(-) Linking "+root+"\\"+file+"...")
                compile_commands = [
                    "gcc",
                    target_obj_path,
                    '-o',
                    "build\\" + subdir_name + ".exe",
                    "-lstdc++"
        
                ]
                subprocess.run(compile_commands)
                print("(!) Linked "+root+"\\"+file+" into "+subdir_name+".exe")

                time.sleep(2);
                
                print("(-) Cleaning Build Cache for "+subdir_name);

                os.remove("build\\"+subdir_name+".o");

                time.sleep(2)
                
                print("(!) Finished Cleaning Build Cache for "+subdir_name);

                

def main():
    src_dir = "src"
    build_dir = "build"
    include_dir = "include"  
    
    compile_files(src_dir, build_dir, include_dir)

if __name__ == "__main__":
    main()
