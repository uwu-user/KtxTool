This should be easy...

---

- Prerequisites
  - Python 3.x
  - pip
  - Git
  - CMake (version 3.10 or higher)
  - C++ compiler (supporting C++11)
  - Make `(Recommended)` or Ninja build system

---

> [!NOTE]
> This one is only for etc2comp so you need to install it first،

> [!IMPORTANT]  
> btw, There is one for each type of ktx `(1.1/2.0)` and more in [uwu-user/pyktx-tool](https://github.com/uwu-user/pyktx-tool)

---
### [ * ]: Compiling etc2comp (Texture Compression Tool, Linux/macOS)

**[1]: Clone the repository**
```
git clone https://github.com/google/etc2comp.git
```

**[2]: Enter the project directory**
```
cd etc2comp
```

**[3]: Create a build directory**
```
mkdir build
```

**[4] Enter the build directory**
```
cd build
```

**[5]: Generate build files with CMake**
```
cmake ..
```

**[6]: compile the project**
```
make -j$(nproc)
```

**[7]: change the permissions**
```
chmod +x ./EtcTool
```

**[ * ]: copy the file** `Optional`
```
copy the EtcTool file from $HOME/etc2comp/build/EtcTool to $HOME
```
 - or you can use a special path when running the tool `(It'll be the same, it won't make a difference)`
```
[ ! ]: EtcTool not found in current directory
   › [ ? ]  Enter the tool path or exit to cancel
      » ./etc2comp/build/EtcTool/EtcTool
```

---
### [ * ] : Compiling etc2comp (Texture Compression Tool, Windows)

**[1]: Clone the repository**
```
git clone https://github.com/google/etc2comp.git
```

**[2]: Enter the project directory**
```
cd etc2comp
```

**[3]: Create a build directory**
```
mkdir build
```

**[4]: Enter the build directory**
```
cd build
```

> [!WARNING]
> To the fact that `etc2comp` has not been updated for a long time, you should change the version on it before building it on windows!
  - open `etc2comp/CMakeLists.txt`
  - change the Version from
    - ```cmake_minimum_required(VERSION 2.8.9)```
  - To
    - ```cmake_minimum_required(VERSION 3.5...3.27)```

**[5]: Generate build files with CMake**
```
cmake ..
```

**[6]: compile the project**
```
cmake --build . --config Release
```

---

If you do everything right, it should be the same as this `[as liunx]`
<p>
    <img src="./assets/etc2comp.png" />
</p>

---

> [!CAUTION]
> If there are any Error,  check [google/etc2comp](https://github.com/google/etc2comp)

--- 

### [ * ]: KtxTool.py Prerequisites

- Tool Prerequisites
  - `os / sys / subprocess / pathlib`
    ```
    python3 built-in module - [Done]
    ```
  - PIL
    ```
    pip install Pillow
    ```

### [3]: KtxTool.py

- clone it
```
wget -O ./ktxtool.py https://raw.githubusercontent.com/uwu-user/KtxTool/main/KtxTool.py
```

- Run it
```
python ktxtool.py
```

- and about the settings just Use the default settings! like:
  
<p>
    <img src="./assets/KtxTool.png" />
</p>

--- 

bye-bye <img src="https://user-images.githubusercontent.com/1303154/88677602-1635ba80-d120-11ea-84d8-d263ba5fc3c0.gif" width="28px" alt="hi">
