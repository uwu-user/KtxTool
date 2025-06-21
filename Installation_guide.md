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
### [1]: Compiling etc2comp (Texture Compression Tool, Linux/macOS)

**- Clone the repository**
```
git clone https://github.com/google/etc2comp.git
```

**- Enter the project directory**
```
cd etc2comp
```

**- Create a build directory**
```
mkdir build
```

**- Enter the build directory**
```
cd build
```

**- Generate build files with CMake**
```
cmake ..
```

**- compile the project**
```
make -j$(nproc)
```

**- change the permissions**
```
chmod +x ./EtcTool
```

**- copy the file**
```
copy the EtcTool file from $HOME/etc2comp/build/EtcTool to $HOME
```

---

If you do everything right, it should be the same as this
<p>
    <img src="./assets/etc2comp.png" />
</p>

---

> [!CAUTION]
> If there are any Error,  check [google/etc2comp](https://github.com/google/etc2comp)

--- 

### [2]: KtxTool.py Prerequisites

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
