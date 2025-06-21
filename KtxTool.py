#______________________________________________________________________________
#     
#     Version v1.0
#     Create by Unknown_#7004 ( @uwu.user )
#         - Github: https://github.com/uwu-user
#         - gamebanana: https://gamebanana.com/members/2496091
#
#______________________________________________________________________________         

# Import required standard library modules
import sys  # System-specific parameters and functions
import subprocess  # Spawning subprocesses
import os  # Operating system interfaces
from pathlib import Path  # Object-oriented filesystem paths
from PIL import Image  # Python Imaging Library for image processing

#______________________________________________________________________________

# ANSI Color Codes class for terminal text formatting
class Colors:
    """
    Provides named constants for ANSI color codes with disable capability.
    Colors can be accessed as class attributes or instance attributes.
    """
    disable_colors = False  # Class-level flag to disable all color output

    # ANSI reset code (always available)
    Reset = "\033[0m"  # Resets all text formatting

    # Internal dictionary of color names and their ANSI codes
    _COLORS = {
    
        # Basic 3/4-bit ANSI colors
        'Black': '\033[30m',  # Standard black color
        'Red': '\033[31m',    # Standard red color
        'Green': '\033[32m',  # Standard green color
        'Yellow': '\033[33m', # Standard yellow color
        'Blue': '\033[34m',   # Standard blue color
        'Magenta': '\033[35m', # Standard magenta color
        'Cyan': '\033[36m',   # Standard cyan color
        'White': '\033[37m',  # Standard white color
        
        # Extended 256-color palette colors
        'Orange': '\033[38;5;208m',  # Orange color from extended palette
        'Pink': '\033[38;5;211m',    # Pink color from extended palette
        
        # Bright color variants
        'Light_Red': '\033[91m',     # Bright red color
        'Light_Green': '\033[92m',   # Bright green color
        'Light_Yellow': '\033[93m',  # Bright yellow color
        'Light_Blue': '\033[94m',    # Bright blue color
        'Light_Magenta': '\033[95m', # Bright magenta color
        'Light_Cyan': '\033[96m',    # Bright cyan color
        'Light_White': '\033[97m',   # Bright white color
        'Light_Grey': '\033[37m',    # Light grey color
    }

    def __init__(self):
        """Initialize instance with color attributes that respect disable_colors"""
        for name, code in self._COLORS.items():  # Iterate through color dictionary
            # Set instance attributes that respect the disable_colors flag
            setattr(self, name, self.Reset if self.disable_colors else code)

    def __getattribute__(self, name):
        """Special method to handle color attribute access dynamically"""
        if name in Colors._COLORS:  # Check if requested attribute is a color
            # Return reset code if colors disabled, otherwise return color code
            return Colors.Reset if Colors.disable_colors else Colors._COLORS[name]
        return super().__getattribute__(name)  # Default attribute access

# Initialize class-level color attributes
for name, code in Colors._COLORS.items():  # Iterate through color dictionary
    # Set class attributes that respect the disable_colors flag
    setattr(Colors, name, Colors.Reset if Colors.disable_colors else code)
            
#______________________________________________________________________________

# File format information class
class Formats:
    """Container for supported file format information"""
    # Dictionary mapping file extensions to (format name, display color) tuples
    FORMATS = {
        '.png': ('PNG', Colors.Light_Blue),  # PNG format with light blue color
        '.jpg': ('JPEG', Colors.Yellow),     # JPEG format with yellow color
        '.jpeg': ('JPEG', Colors.Yellow),    # JPEG format with yellow color
    }

#______________________________________________________________________________

# Function to display tool logo and information
def print_tool_logo():
    """Prints the tool's logo and version information in a formatted box"""
    clear_console()  # Clear terminal before displaying logo
    # Multi-line formatted string with color codes and box-drawing characters
    print(f"""{Colors.Light_Blue}  
╭───────────────────────────────────────╮  
│ {Colors.Cyan}» {Colors.White}ETC Tool{Colors.White}{' ' * 28}{Colors.Light_Blue}│  
│ {Colors.Cyan}» {Colors.White}Version {Colors.Green}1.0{Colors.White}{' ' * 25}{Colors.Light_Blue}│  
╰───────────────────────────────────────╯  
{Colors.White}{' ' * 1}› {Colors.White}[ {Colors.Cyan}? {Colors.White}] {Colors.Green}Bug's reporting: \n{' ' * 3}› {Colors.White}https://{Colors.Green}github.com{Colors.White}/{Colors.Light_Cyan}uwu-user{Colors.White}/{Colors.Light_Blue}KtxTool{Colors.White}/issues/New
{Colors.Reset}""")

#______________________________________________________________________________

# Function to clear terminal screen
def clear_console():
    """Clears the terminal screen safely on Windows, macOS, and Linux."""
    # Run 'cls' on Windows, 'clear' on Unix/macOS
    subprocess.run(["cls"] if os.name == "nt" else ["clear"], check=True)
    
#______________________________________________________________________________

# Function to convert bytes to human-readable format
def convert_bytes(size):
    """Converts byte size to human-readable string with appropriate units"""
    if size >= 1024 * 1024:  # Check for megabyte range
        return f"{size / (1024 * 1024):.2f} MB"  # Convert to MB with 2 decimals
    elif size >= 1024:  # Check for kilobyte range
        return f"{size / 1024:.2f} KB"  # Convert to KB with 2 decimals
    return f"{size} bytes"  # Default to bytes for small sizes

#______________________________________________________________________________

# Function to verify tool executable
def verify_etctool():
    """Verifies existence and permissions of EtcTool.so"""
    toolpath = Path("./EtcTool.so")  # Create Path object for the tool
    
    if not toolpath.exists():  # Check if file doesn't exist
        # Print error message in red box
        print(f"\n{Colors.Red}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Red}Tool Not Found:{Colors.Reset}")
        print(f"{Colors.Reset}╭─────────────────────────────────────────────╮")
        print(f"{Colors.Reset}│ {Colors.Light_Blue}EtcTool.so {Colors.Red}not found in working directory{' ' * 3}{Colors.Reset}│")
        print(f"{Colors.Reset}╰─────────────────────────────────────────────╯")
        return None  # Return None indicating failure

    try:
        toolpath = toolpath.resolve()  # Convert to absolute path
        tool_size = toolpath.stat().st_size  # Get file size in bytes
        size_str = convert_bytes(tool_size)  # Convert size to readable format
        
        if not toolpath.is_file() or not os.access(toolpath, os.X_OK):  # Check permissions
            # Print permission error in red/white box
            print(f"\n{Colors.Red}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Red}Permission Issue:{Colors.Reset}")
            print(f"{Colors.White}╭─────────────────────────────────────────────╮")
            print(f"{Colors.White}│ {Colors.Red}Found tool but missing execute permissions{' ' * 2}{Colors.White}│")
            print(f"{Colors.White}│ {Colors.White}Size: {Colors.Green}{size_str.ljust(36)}{Colors.White}│")
            print(f"{Colors.White}├─────────────────────────────────────────────┤")
            print(f"{Colors.White}│ {Colors.White}Use: {Colors.Green}chmod +x {toolpath}{' ' * (30-len(str(toolpath)))}{Colors.White}│")
            print(f"{Colors.White}╰─────────────────────────────────────────────╯")
            return None  # Return None indicating permission failure

        # Print success message in green box
        print(f"\n{Colors.Green}• {Colors.White}[ {Colors.Light_Blue}✓ {Colors.White}]: {Colors.Green}Tool Verification{Colors.Reset}")
        print(f"{Colors.Green}╭─────────────────────────────────────────────╮")
        print(f"{Colors.Green}│ {Colors.Light_Blue}EtcTool.so {Colors.Green}verified and ready for use{' ' * 7}{Colors.Green}│")
        print(f"{Colors.Green}│ {Colors.Light_Blue}Size{Colors.Light_Blue}: {Colors.Green}{size_str.ljust(38)}{Colors.Green}│")
        print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
        return str(toolpath)  # Return absolute path string on success
        
    except Exception as e:  # Catch any unexpected errors
        # Print error details in red box
        print(f"\n{Colors.Red}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Red}Verification Failed:{Colors.Reset}")
        print(f"{Colors.Red}╭─────────────────────────────────────────────╮")
        print(f"{Colors.Red}│ {Colors.White}Error: {Colors.Yellow}{str(e)}{' ' * (37-len(str(e)))}{Colors.Red}│")
        print(f"{Colors.Red}╰─────────────────────────────────────────────╯")
        return None  # Return None indicating verification failure

#______________________________________________________________________________

# File Handling
def check_file(file, file_type, cmd_type):
    """
    Validates input/output files with automatic extension handling.
    
    Args:
        file (str): Path to the file to check
        file_type (int): 1 for input file, 2 for output file
        cmd_type (int): Command type for different display modes
    
    Returns:
        bool: True if validation passes, False otherwise
    
    Raises:
        FileNotFoundError: If input file doesn't exist
        FileExistsError: If output file already exists
    """
    try:
        file_path = Path(file)  # Convert string path to Path object
        
        # Auto-add extension if missing by checking supported formats
        if not any(file_path.suffix.lower() == ext for ext in Formats.FORMATS.keys()):  # Check if extension is missing
            for ext in Formats.FORMATS.keys():  # Iterate through supported extensions
                test_path = file_path.with_suffix(ext)  # Create path with test extension
                if test_path.exists():  # Check if file with this extension exists
                    file_path = test_path  # Use the found path
                    break  # Stop after first match
        
        if file_type == 1:  # Input file validation
            if file_path.exists():  # Check if file exists
                if cmd_type == 1:  # Detailed output mode
                    size = convert_bytes(file_path.stat().st_size)  # Get human-readable size
                    print(f"\n {Colors.Green} › [ found it  {Colors.Reset}] {Colors.Reset}")  # Success message
                    print(f"{Colors.Green}╭─────────────────────────────────────────────╮")  # Top border
                    print(f"{Colors.Green}│ {Colors.White}Path{Colors.Light_Blue}: {Colors.Green}{str(file_path).ljust(36)}{Colors.Reset}  {Colors.Green}│")  # File path
                    print(f"{Colors.Green}│ {Colors.White}Size{Colors.Light_Blue}: {Colors.Green}{size.ljust(36)}{Colors.Reset}  {Colors.Green}│")  # File size
                    print(f"{Colors.Green}╰─────────────────────────────────────────────╯")  # Bottom border
                return True  # Validation passed
            raise FileNotFoundError(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}{file_path} {Colors.Red}not found!{Colors.Reset}")  # Error if file missing
        
        elif file_type == 2:  # Output file validation
            if not file_path.exists():  # Check if file doesn't exist
                if cmd_type == 1:  # Detailed output mode
                    print(f"\n › [ {Colors.Green}A {Colors.Light_Blue}.KTX {Colors.Green}repository will be created ] {Colors.Reset}")  # Info message
                    print(f"{Colors.Green}╭─────────────────────────────────────────────╮")  # Top border
                    print(f"{Colors.Green}│ {Colors.White}File{Colors.Light_Blue}: {Colors.Green}{str(file_path).ljust(40)}{Colors.Reset}  {Colors.Green}│")  # Output path
                    print(f"{Colors.Green}╰─────────────────────────────────────────────╯")  # Bottom border
                return True  # Validation passed
            raise FileExistsError(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}{file_path} {Colors.Green}already exists!{Colors.Reset}\n")  # Error if file exists
    
    except Exception as e:  # Catch any unexpected errors
        print(str(e))  # Print error message
        return False  # Validation failed

#______________________________________________________________________________

# Supported files
def get_supported_files(folder_path):
    """
    Scan a directory for supported image files.
    
    Args:
        folder_path (str): Path to directory to scan
        
    Returns:
        list: List of strings containing paths to supported files
    
    Example:
        » get_supported_files('/path/to/images')
        ['/path/to/images/image1.png', '/path/to/images/image2.jpg']
    """
    folder = Path(folder_path)  # Convert to Path object
    supported_files = []  # Initialize empty list for results
    
    for ext in Formats.FORMATS.keys():  # Iterate through supported extensions
        supported_files.extend(folder.glob(f"*{ext}"))  # Find all files with this extension
    
    return [str(f) for f in supported_files]  # Convert Path objects to strings

#______________________________________________________________________________

# ETC Texture Compression Configuration Functions
"""
Provides interactive menus for configuring ETC texture compression settings including:
- Format selection
- Error metrics
- Compression options
Handles user input validation and provides color-coded interface feedback.
"""

#______________________________________________________________________________

# Exit cmd
def check_for_exit(input_str):
    """Check if user wants to exit and exit if so"""
    if input_str.lower() == 'exit':  # Check for exit command
        print(f"\n{Colors.Cyan}• {Colors.Reset}[ {Colors.Green}Shutting down... {Colors.Reset}]{Colors.Reset}")  # Exit message
        # should I say Exiting program or Shutting down or Exiting or what?
        sys.exit(0)  # Clean exit
    return input_str  # Return original string if not exiting

#______________________________________________________________________________

# import format
def get_etc_format():
    """
    Interactive menu for ETC format selection.
    
    Returns:
        str: Selected format code (e.g. 'RGBA8')
    """
    # Available ETC formats with color-coded descriptions
    formats = {
        1: ("ETC1", f"{Colors.White}ETC1 {Colors.Light_Blue}compression {Colors.White}({Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.White} only){Colors.Reset}"),  # ETC1 format
        2: ("RGB8", f"{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.White} 8-bit {Colors.Light_Blue}per channel {Colors.White}({Colors.Cyan}no alpha{Colors.White}){Colors.Reset}"),  # RGB8 format
        3: ("SRGB8", f"{Colors.Yellow}s{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B {Colors.Light_Blue}color space {Colors.White}({Colors.Orange}gamma corrected{Colors.White}){Colors.Reset}"),  # sRGB format
        4: ("RGBA8", f"{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.Magenta}A {Colors.White}8-bit {Colors.Light_Blue}per channel {Colors.White}({Colors.Green}full alpha{Colors.White}){Colors.Reset}"),  # RGBA8 format
        5: ("SRGBA8", f"{Colors.Yellow}s{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.Magenta}A {Colors.White}({Colors.Orange}gamma{Colors.White} + {Colors.Pink}alpha{Colors.White}){Colors.Reset}"),  # sRGBA format
        6: ("RGB8A1", f"{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.White}8{Colors.Magenta}A1 {Colors.White}({Colors.Light_Red}1-bit alpha{Colors.White}){Colors.Reset}"),  # RGB8A1 format
        7: ("SRGB8A1", f"{Colors.Yellow}s{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B{Colors.White}8{Colors.Magenta}A1 {Colors.White}({Colors.Orange}gamma{Colors.White} + {Colors.Light_Red}1-bit alpha{Colors.White}){Colors.Reset}"),  # sRGB8A1 format
        8: ("R11", f"{Colors.Red}R11 {Colors.Light_Blue}single-channel {Colors.White}({Colors.Cyan}11-bit{Colors.White}){Colors.Reset}")  # R11 format
    }

    print(f"\n{Colors.Cyan}• {Colors.Green}[3/5]: {Colors.White}Select ETC format:{Colors.Reset}")  # Menu header
    for num, (fmt, desc) in formats.items():  # Display all format options
        print(f"{' ' * 3}{Colors.Green}{num:2}{Colors.Reset}. › {Colors.Light_Blue}{fmt.ljust(10)}{Colors.Reset} - {desc}")
    
    while True:  # Input loop
        try:
            choice = input(f"{' ' * 7}› {Colors.Green}( default {Colors.White}= {Colors.Green}4{Colors.Reset}. › {Colors.Light_Blue}RGBA8 {Colors.Green})\n{' ' * 7}{Colors.Green}» ")  # Prompt
            choice = check_for_exit(choice)  # Check for exit command
            if not choice:  # Handle default selection
                selected = "RGBA8"  # Default format
                print(f"\n")
                print(f"{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
                print(f"{Colors.Green}│ {Colors.White}Using the default format{Colors.Light_Blue}: {Colors.Green}{selected.ljust(17)}{Colors.Reset} {Colors.Green}│")
                print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
                return selected  # Return default
            choice = int(choice)  # Convert to integer
            if choice in formats:  # Validate choice
                selected = formats[choice][0]  # Get format code
                desc = formats[choice][1].replace(Colors.Reset, "").replace(Colors.Light_Blue, "")  # Clean description
                print(f"\n")
                print(f"{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
                print(f"{Colors.Green}│ {Colors.White}Using format{Colors.Light_Blue}: {Colors.Green}{selected.ljust(29)}{Colors.Reset} {Colors.Green}│")
                print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
                return selected  # Return selected format
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Invalid choice. Enter {Colors.Green}1-8 {Colors.Light_Blue}or {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.Light_Blue}to cancel{Colors.Reset}")  # Error message
        except ValueError:  # Handle non-numeric input
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Enter a number{Colors.Reset}")

#______________________________________________________________________________

# import metric
def get_error_metric():
    """
    Interactive menu for error metric selection.
    
    Returns:
        str: Selected metric code (e.g. 'rgba')
    """
    # Available error metrics with descriptions
    metrics = {
        1: ("rgba", f"{Colors.Green}Standard RGBA{Colors.Reset}"),  # RGBA metric
        2: ("rgbx", f"{Colors.Red}R{Colors.Green}G{Colors.Light_Blue}B {Colors.Light_Grey}(ignore alpha){Colors.Reset}"),  # RGBX metric
        3: ("rec709", f"{Colors.Yellow}Rec.709 luminance{Colors.Reset}"),  # Rec.709 metric
        4: ("numeric", f"{Colors.Cyan}Numeric difference{Colors.Reset}"),  # Numeric metric
        5: ("normalxyz", f"{Colors.Magenta}Normal maps{Colors.Reset}")  # Normal map metric
    }
    
    print(f"\n{Colors.Cyan}• {Colors.Green}[4/5]: {Colors.White}Select error metric:{Colors.Reset}")  # Menu header
    for num, (code, desc) in metrics.items():  # Display all metric options
        print(f"{' ' * 4}{Colors.Green}{num}. {Colors.Reset}› {Colors.Light_Blue}{code.ljust(8)}{Colors.White} - {Colors.Yellow}{desc}{Colors.Reset}")
    print(f"{' ' * 7}{Colors.White}›  {Colors.Green}( default {Colors.White}= {Colors.Green}1{Colors.Reset}. › {Colors.Light_Blue}rgba {Colors.Green}){Colors.Reset}")  # Default hint
    
    while True:  # Input loop
        try:
            choice = input(f"{' ' * 7}{Colors.Green}» ")  # Prompt
            choice = check_for_exit(choice)  # Check for exit command
            if not choice:  # Handle default selection
                selected = "rgba"  # Default metric
                print(f"\n{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
                print(f"{Colors.Green}│ {Colors.White}Using the default metric{Colors.Light_Blue}: {Colors.Green}{selected.ljust(17)}{Colors.Reset} {Colors.Green}│")
                print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
                return selected  # Return default
            choice = int(choice)  # Convert to integer
            if choice in metrics:  # Validate choice
                selected = metrics[choice][0]  # Get metric code
                print(f"\n{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
                print(f"{Colors.Green}│ {Colors.White}Using metric{Colors.Light_Blue}: {Colors.Green}{selected.ljust(29)}{Colors.Reset} {Colors.Green}│")
                print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
                return selected  # Return selected metric
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Invalid choice. Enter {Colors.Green}1-5 {Colors.Light_Blue}or {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.Light_Blue}to cancel{Colors.Reset}")  # Error message
        except ValueError:  # Handle non-numeric input
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Enter a number{Colors.Reset}")

#______________________________________________________________________________

# Additional options
def get_additional_options():
    """
    Interactive menu for advanced compression settings.
    
    Returns:
        list: Command line options for compression settings
    """
    options = []  # List to store selected options
    
    print(f"\n{Colors.Cyan}• {Colors.Green}[5/5]: {Colors.White}Compression Settings:{Colors.Reset}")  # Menu header
    
    # Effort level setting
    print(f"{' ' * 4}{Colors.Cyan}• {Colors.Green}[1/3] {Colors.Light_Blue}Compression effort {Colors.White}({Colors.Green}1{Colors.White}-{Colors.Green}100{Colors.White}){Colors.Reset}")  # Submenu
    print(f"{' ' * 7}{Colors.Orange}› {Colors.Orange}[ {Colors.Red}Note {Colors.Orange}]{Colors.Light_Blue}: {Colors.Green}Higher values {Colors.White}= {Colors.Green}better quality but {Colors.Red}slower {Colors.White}[{Colors.Light_Blue}default: {Colors.Green}50{Colors.White}]{Colors.Reset}")  # Help text
    effort = get_valid_input(  # Get validated input
        prompt=f"{' ' * 7}{Colors.Green}» ",
        validation=lambda x: x.isdigit() and 1 <= int(x) <= 100,  # Validation rule
        error_msg=f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Enter a value between {Colors.Green}1-100{Colors.Reset}",  # Error message
        default="50"  # Default value
    )
    if effort:  # If valid input received
        options.extend(["-effort", effort])  # Add to options
        print(f"\n{' ' * 4}{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
        print(f"{' ' * 4}{Colors.Green}│ {Colors.White}Use effort{Colors.Light_Blue}: {Colors.Green}{effort.ljust(31)}{Colors.Reset} {Colors.Green}│")
        print(f"{' ' * 4}{Colors.Green}╰─────────────────────────────────────────────╯")

    # Mipmap levels setting
    print(f"\n{' ' * 4}{Colors.Cyan}• {Colors.Green}[2/3] {Colors.Light_Blue}Mipmap levels {Colors.White}({Colors.Green}0{Colors.White}-{Colors.Green}11{Colors.White}){Colors.Reset}")  # Submenu
    print(f"{' ' * 7}{Colors.Orange}› {Colors.Orange}[ {Colors.Red}Note {Colors.Orange}]{Colors.Light_Blue}: {Colors.Green}0 {Colors.White}= {Colors.Red}no {Colors.Light_Blue}mipmaps{Colors.White}, {Colors.Green}11 {Colors.White}= {Colors.Light_Blue}maximum {Colors.White}[{Colors.Light_Blue}default: {Colors.Green}11{Colors.White}]{Colors.Reset}")  # Help text
    mips = get_valid_input(  # Get validated input
        prompt=f"{' ' * 7}{Colors.Green}» ",
        validation=lambda x: x.isdigit() and 0 <= int(x) <= 11,  # Validation rule
        error_msg=f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Enter a value between {Colors.Green}0-11{Colors.Reset}",  # Error message
        default="11"  # Default value
    )
    if mips:  # If valid input received
        options.extend(["-mipmaps", mips])  # Add to options
        print(f"\n{' ' * 4}{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
        print(f"{' ' * 4}{Colors.Green}│ {Colors.White}Use mipmaps{Colors.Light_Blue}: {Colors.Green}{mips.ljust(30)}{Colors.Reset} {Colors.Green}│")
        print(f"{' ' * 4}{Colors.Green}╰─────────────────────────────────────────────╯")

    # Verbose mode setting
    print(f"\n{' ' * 4}{Colors.Cyan}• {Colors.Green}[3/3] {Colors.Light_Blue}Verbose output {Colors.White}({Colors.Green}y{Colors.White}/{Colors.Red}n{Colors.White}){Colors.Reset}")  # Submenu
    print(f"{' ' * 7}{Colors.Orange}› {Colors.Orange}[ {Colors.Red}Note {Colors.Orange}]{Colors.Light_Blue}: {Colors.Yellow}Show detailed conversion progress {Colors.White}[{Colors.Light_Blue}default: {Colors.Red}n{Colors.White}]{Colors.Reset}")  # Help text
    verbose = get_valid_input(  # Get validated input
        prompt=f"{' ' * 7}{Colors.Green}» ",
        validation=lambda x: x.lower() in ('y', 'n', ''),  # Validation rule
        error_msg=f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Enter {Colors.White}({Colors.Green}y{Colors.White}/{Colors.Red}n{Colors.White}){Colors.Reset}",  # Error message
        default="n"  # Default value
    )
    if verbose.lower() == 'y':  # If verbose enabled
        options.append("-verbose")  # Add verbose flag
        print(f"\n{' ' * 4}{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
        print(f"{' ' * 4}{Colors.Green}│ {Colors.White}Use verbose{Colors.Light_Blue}: {Colors.Green}yes{' ' * 27}{Colors.Reset} {Colors.Green}│")
        print(f"{' ' * 4}{Colors.Green}╰─────────────────────────────────────────────╯")
    else:  # If verbose disabled
        print(f"\n{' ' * 4}{Colors.Green}╭─────────────────────────────────────────────╮")  # Success box
        print(f"{' ' * 4}{Colors.Green}│ {Colors.White}Use verbose{Colors.Light_Blue}: {Colors.Red}no{' ' * 28}{Colors.Reset} {Colors.Green}│")
        print(f"{' ' * 4}{Colors.Green}╰─────────────────────────────────────────────╯")
        
    return options  # Return all selected options

#______________________________________________________________________________

# input things
def get_valid_input(prompt, validation, error_msg, default=""):
    """
    Generic input validation helper with default value support.
    
    Args:
        prompt (str): The input prompt to display
        validation (function): Validation function that returns True/False
        error_msg (str): Error message to show when validation fails
        default (str): Default value to return if input is empty (default: "")
        
    Returns:
        str: Validated user input or default value
        
    Features:
        - Handles empty input by returning default value
        - Supports exit command via check_for_exit()
        - Repeats prompt until valid input received
        - Provides consistent error messaging
    """
    while True:  # Keep prompting until valid input received
        user_input = input(prompt).strip()  # Get and clean user input
        user_input = check_for_exit(user_input)  # Check for exit command
        
        # Return default if input empty and default specified
        if not user_input and default:  # Check for empty input with default available
            return default  # Return default value
            
        # Validate the input
        if validation(user_input):  # Run validation function
            return user_input  # Return valid input
            
        # Show error message if validation fails
        print(error_msg)  # Display formatted error message

#______________________________________________________________________________

# Conversion Core
def convert_image_to_ktx(input_file, output_file, etc_format, error_metric, options, toolpath):
    """
    Convert an image file to KTX format using EtcTool.
    
    Args:
        input_file (str): Path to source image file
        output_file (str): Path for output KTX file
        etc_format (str): ETC compression format (e.g. 'RGBA8')
        error_metric (str): Error metric for compression quality
        options (list): Additional command line options
        toolpath (str): Path to EtcTool executable
        
    Returns:
        bool: True if conversion succeeded, False otherwise
        
    Raises:
        RuntimeError: If output file isn't created after conversion
        subprocess.CalledProcessError: If EtcTool fails
    """
    try:
        # Convert paths to Path objects for consistent handling
        input_path = Path(input_file)  # Source image path
        output_path = Path(output_file)  # Destination KTX path
        
        # Verify input image and get metadata
        with Image.open(input_path) as img:  # Open image using PIL
            width, height = img.size  # Extract image dimensions
            orig_size = input_path.stat().st_size  # Get original file size
        
        # Build EtcTool command with all parameters
        cmd = [
            toolpath,  # Path to EtcTool executable
            str(input_path),  # Input file path
            "-format", etc_format,  # Compression format
            "-errormetric", error_metric,  # Quality metric
            "-output", str(output_path)  # Output file path
        ] + options  # Additional compression options
        
        # Execute conversion with progress tracking
        result = subprocess.run(
            cmd, 
            check=True,  # Raise exception on failure
            capture_output=True,  # Capture output for error handling
            text=True  # Return output as text
        )
        
        # Verify output file was created
        if not output_path.exists():  # Check output file existence
            raise RuntimeError(f"{Colors.Red}Conversion failed - no output file created{Colors.Reset}")
        
        # Calculate and display conversion results
        new_size = output_path.stat().st_size  # Get output file size
        print(f"{Colors.Green}╭─────────────────────────────────────────────╮")  # Results box top
        print(f"{Colors.Green}│ {Colors.White}Conversion Successful!{' ' * 22}{Colors.Green}│")  # Success message
        print(f"{Colors.Green}├─────────────────────────────────────────────┤")  # Separator
        print(f"{Colors.Green}│ {Colors.White}File{Colors.Light_Blue}: {Colors.Green}{input_path.name.ljust(38)}{Colors.Green}│")  # Input filename
        print(f"{Colors.Green}│ {Colors.White}Dimensions{Colors.Light_Blue}: {Colors.Green}{width}x{height}{' ' * (32-len(f'{width}x{height}'))}{Colors.Green}│")  # Image size
        print(f"{Colors.Green}│ {Colors.White}Input Size{Colors.Light_Blue}: {Colors.Green}{convert_bytes(orig_size).ljust(32)}{Colors.Green}│")  # Original size
        print(f"{Colors.Green}│ {Colors.White}Output Size{Colors.Light_Blue}: {Colors.Green}{convert_bytes(new_size).ljust(31)}{Colors.Green}│")  # Compressed size
        print(f"{Colors.Green}╰─────────────────────────────────────────────╯\n{Colors.Reset}")  # Box bottom
        
        return True  # Indicate success
        
    except subprocess.CalledProcessError as e:
        # Handle EtcTool execution errors
        print(f"\n{Colors.Red}╭─────────────────────────────────────────────╮")  # Error box top
        print(f"{Colors.Red}│ {Colors.White}Conversion Failed{' ' * 35}{Colors.Red}│")  # Error header
        print(f"{Colors.Red}├─────────────────────────────────────────────┤")  # Separator
        print(f"{Colors.Red}│ {Colors.White}Error Output:{Colors.Reset}")  # Error label
        print(f"{Colors.Red}│ {Colors.Yellow}{e.stderr}{Colors.Red}│")  # Actual error message
        print(f"{Colors.Red}╰─────────────────────────────────────────────╯\n{Colors.Reset}")  # Box bottom
        return False  # Indicate failure
        
    except Exception as e:
        # Handle unexpected errors
        print(f"{Colors.Red}[ ! ] Critical Error: {Colors.White}{str(e)}{Colors.Reset}")  # Compact error message
        return False  # Indicate failure

#______________________________________________________________________________

# Folder Mode
def convert_folder(input_folder, etc_format, error_metric, options, toolpath):
    """
    Batch convert all supported image files in a folder to KTX format.
    
    Args:
        input_folder (str): Path to folder containing source images
        etc_format (str): ETC compression format (e.g. 'RGBA8')
        error_metric (str): Error metric for compression quality
        options (list): Additional command line options
        toolpath (str): Path to EtcTool executable
        
    Returns:
        - conversions files
        
    Features:
        - Interactive overwrite prompts for existing files
        - Bulk operation options (skip all/overwrite all)
        - Progress tracking with file counters
        - Detailed conversion statistics
    """
    input_path = Path(input_folder)
    if not input_path.is_dir():  # Validate input directory
        print(f"{Colors.Red}[ ! ] Error: {Colors.White}{input_folder} {Colors.Red}is not a valid directory!{Colors.Reset}")
        return False
    
    # Get list of supported image files
    supported_files = get_supported_files(input_folder)
    if not supported_files:  # Check if any convertible files found
        print(f"\n{Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: No supported files found in {Colors.Light_Blue}{input_folder}{Colors.Reset}")
        return False
    
    # Display file count summary
    print(f"\n{Colors.Cyan}• {Colors.White}[ {Colors.Light_Blue}Loading... {Colors.White}] {Colors.Reset}")
    print(f"{Colors.Green}╭─────────────────────────────────────────────╮")
    print(f"{Colors.Green}│ {Colors.White}Found {len(supported_files)} files to convert{' ' * 20}{Colors.Green}│")
    print(f"{Colors.Green}╰─────────────────────────────────────────────╯\n{Colors.Reset}")
    
    # Initialize counters and flags
    skip_all = False  # Global skip flag
    overwrite_all = False  # Global overwrite flag
    success_count = 0  # Successful conversions
    skipped_count = 0  # Skipped files
    failed_count = 0  # Failed conversions

    # Process each file with progress counter
    for i, input_file in enumerate(supported_files, 1):
        input_path = Path(input_file)
        ktx_file = input_path.with_suffix('.ktx')  # Generate output path
        
        # Handle existing output files
        if ktx_file.exists():
            if skip_all:  # Skip if global skip enabled
                print(f"{Colors.Cyan}• {Colors.White}[ {Colors.Yellow}Skipping: {Colors.Light_Blue}{input_path.name} {Colors.White}]{Colors.Reset}")
                skipped_count += 1
                continue
            if overwrite_all:  # Overwrite if global flag set
                print(f"{Colors.Cyan}• {Colors.White}[ {Colors.Red}Overwriting: {Colors.Green}{input_path.name} {Colors.White}]{Colors.Reset}")
            else:
                # Interactive prompt for conflict resolution
                print(f"\n{Colors.Yellow}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Yellow}Output file {Colors.Green}already exists{Colors.Reset}")
                print(f"{Colors.Yellow}╭─────────────────────────────────────────────╮")
                print(f"{Colors.Yellow}│ {Colors.White}File{Colors.Light_Blue}: {Colors.Yellow}{ktx_file.name.ljust(36)}{Colors.Reset}  {Colors.Yellow}│")
                print(f"{Colors.Yellow}╰─────────────────────────────────────────────╯")
                
                # Display conflict resolution options
                print(f"{' ' * 4}{Colors.Green}› {Colors.Light_Blue}Action's: {Colors.Reset}")
                print(f"{' ' * 7}{Colors.Green}1{Colors.Reset}. › {Colors.Light_Blue}Overwrite this file{Colors.Reset}")
                print(f"{' ' * 7}{Colors.Green}2{Colors.Reset}. › {Colors.Light_Blue}Skip this file{Colors.Reset}")
                print(f"{' ' * 7}{Colors.Green}3{Colors.Reset}. › {Colors.Light_Blue}Overwrite {Colors.Red}[ all remaining files ]{Colors.Reset}")
                print(f"{' ' * 7}{Colors.Green}4{Colors.Reset}. › {Colors.Light_Blue}Skip {Colors.Green}[ all remaining files ]{Colors.Reset}")
                
                # Get and validate user choice
                while True:
                    try:
                        choice = input(f"\n{' ' * 9}{Colors.Green}» ")
                        choice = check_for_exit(choice)
                        
                        if not choice.isdigit():  # Validate numeric input
                            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Invalid choice. Enter {Colors.Green}1{Colors.White}-{Colors.Green}4 {Colors.Light_Blue}or {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.Light_Blue}to cancel{Colors.Reset}")
                            continue
                            
                        choice_num = int(choice)
                        if choice_num == 1:  # Overwrite single file
                            break
                        elif choice_num == 2:  # Skip single file
                            print(f"{' ' * 11}› {Colors.White}[ {Colors.Light_Blue}? {Colors.White}] {Colors.Yellow}Skipping: {Colors.Green}{input_path.name}{Colors.Reset}")
                            skipped_count += 1
                            break
                        elif choice_num == 3:  # Overwrite all remaining
                            overwrite_all = True
                            print(f"{' ' * 11}› {Colors.White}[ {Colors.Light_Blue}? {Colors.White}] {Colors.Red}Will overwrite all remaining files\n{Colors.Reset}")
                            break
                        elif choice_num == 4:  # Skip all remaining
                            skip_all = True
                            skipped_count += 1
                            print(f"{' ' * 11}› {Colors.White}[ {Colors.Light_Blue}? {Colors.White}] {Colors.Green}Skipping all remaining files\n{Colors.Reset}")
                            break
                        else:  # Invalid number
                            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Invalid choice. Enter {Colors.Green}1-4{Colors.Reset}")
                            continue
                            
                    except ValueError:  # Handle non-numeric input
                        print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.Light_Blue}Invalid choice. Enter {Colors.Green}1-4{Colors.Reset}")
                        continue
                
                if skip_all or choice_num in (2, 4):  # Skip if chosen
                    continue
        
        # Convert current file
        print(f"{Colors.Cyan}• {Colors.White}[ {Colors.Green}Converting {Colors.Light_Blue}[{i}/{len(supported_files)}]: {Colors.Green}{input_path.name}... {Colors.White}]{Colors.Reset}")
        if convert_image_to_ktx(str(input_path), str(ktx_file), etc_format, error_metric, options, toolpath):
            success_count += 1  # Increment success counter
        else:
            failed_count += 1  # Increment failure counter

    # Calculate skipped files (may differ from prompts due to failures)
    skipped_count = len(supported_files) - success_count - failed_count
    
    # Display final conversion report
    print(f"\n{Colors.Green}• {Colors.White}[ {Colors.Light_Blue}✓ {Colors.White}]: {Colors.Green}Done.{Colors.Reset}")    
    print(f"{Colors.Green}╭─────────────────────────────────────────────╮")
    print(f"{Colors.Green}│ {Colors.White}Total Files{Colors.Light_Blue}: {Colors.Green}{len(supported_files)}{' ' * (31-len(str(len(supported_files))))}{Colors.Green}│")
    print(f"{Colors.Green}│ {Colors.White}Successful{Colors.Light_Blue}: {Colors.Green}{success_count}{' ' * (32-len(str(success_count)))}{Colors.Green}│")
    print(f"{Colors.Green}│ {Colors.White}Skipped{Colors.Light_Blue}: {Colors.Green}{skipped_count}{' ' * (35-len(str(skipped_count)))}{Colors.Green}│")
    print(f"{Colors.Green}│ {Colors.White}Failed{Colors.Light_Blue}: {Colors.Green}{failed_count}{' ' * (36-len(str(failed_count)))}{Colors.Green}│")
    print(f"{Colors.Green}╰─────────────────────────────────────────────╯{Colors.Reset}")
    
    return success_count > 0  # Return True if any conversions succeeded
    
#______________________________________________________________________________

# Main Workflow, Image Conversion Workflow Handler
# Guides users through the entire conversion process with menu prompts
# Handles both file and folder conversion paths
def launch_interactive_converter():
    """Main entry point for interactive conversion mode
    Guides user through step-by-step conversion process with menus and prompts"""
    print_tool_logo()  # Display the tool's logo/header
    
    # Verify EtcTool.so is available
    toolpath = verify_etctool()  
    if not toolpath:
        print(f"\n{Colors.Red}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Red}Cannot continue without EtcTool.so{Colors.Reset}")
        check_for_exit("exit")  # Exit if critical dependency missing
    
    # Present conversion type options
    print(f"\n{Colors.Cyan}• {Colors.Green}[1/5]: {Colors.White}Select input type: \n › {Colors.Orange}[ {Colors.Red}Note {Colors.Orange}]{Colors.White}: type {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.White}to cancel{Colors.Reset}")
    print(f"{' ' * 4}{Colors.Green}1. {Colors.Reset}› {Colors.Light_Blue}Single file{Colors.Reset}")  # Option 1: Single file
    print(f"{' ' * 4}{Colors.Green}2. {Colors.Reset}› {Colors.Light_Blue}Folder {Colors.Green}(Multiple files){Colors.Reset}")  # Option 2: Batch folder
    
    # Process user selection
    while True:
        choice = input(f"{' ' * 7}{Colors.Green}» ")  # Get user input
        choice = check_for_exit(choice)  # Check for exit command
        if choice == '1':
            return process_single_file_conversion(toolpath)  # Handle single file
        elif choice == '2':
            return process_folder_conversion(toolpath)  # Handle folder batch
        # Invalid input handling
        print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Enter 1 or 2 or {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.White}to cancel{Colors.Reset}\n")

#______________________________________________________________________________

# Single file conversion processor
# Handles all steps for converting individual image files:
# 1. Input file validation
# 2. Output file handling
# 3. Conversion parameter collection
# 4. Actual conversion execution
def process_single_file_conversion(toolpath):
    """Handles conversion workflow for individual image files
    Args:
        toolpath: Path to EtcTool.so binary"""
    while True:
        # Get input file path from user
        input_file = input(f"\n{Colors.Cyan}• {Colors.Green}[2/5]: {Colors.White}Enter the input filename\n › {Colors.Orange}[ {Colors.Red}Note {Colors.Orange}]{Colors.White}: type {Colors.Red}'{Colors.Green}exit{Colors.Red}' {Colors.White}to cancel\n{' ' * 3}{Colors.Green}» ")
        input_file = check_for_exit(input_file)  # Check for exit command
        
        # Validate input
        if not input_file:
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] Enter a filename{Colors.Reset}")
            continue
        
        # Handle missing file extensions
        input_path = Path(input_file)
        if not any(input_path.suffix.lower() == ext for ext in Formats.FORMATS.keys()):
            for ext in Formats.FORMATS.keys():  # Try common extensions
                test_path = input_path.with_suffix(ext)
                if test_path.exists():
                    input_path = test_path
                    break
        
        # Verify file exists and is valid
        if check_file(str(input_path), 1, 1):
            break
    
    # Set output path (same name with .ktx extension)
    output_path = input_path.with_suffix('.ktx')
    
    # Handle existing output files
    if output_path.exists():
        print(f"\n{Colors.Yellow}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Yellow}Output file {Colors.Green}already exists{Colors.Reset}")
        print(f"{Colors.Yellow}╭─────────────────────────────────────────────╮")
        print(f"{Colors.Yellow}│ {Colors.White}File{Colors.Light_Blue}: {Colors.Yellow}{output_path.name.ljust(36)}{Colors.Reset}  {Colors.Yellow}│")
        print(f"{Colors.Yellow}╰─────────────────────────────────────────────╯")
        
        # Prompt for overwrite confirmation
        overwrite = input(f"{' ' * 3}{Colors.Yellow}» Overwrite existing file? {Colors.Light_Blue}({Colors.Green}y{Colors.Light_Blue}/{Colors.Red}n{Colors.Light_Blue}): {Colors.Green}").lower()
        overwrite = check_for_exit(overwrite)
        if overwrite != 'y':
            print(f"\n{Colors.Green}• {Colors.White}[ {Colors.Light_Blue}✓ {Colors.White}]: {Colors.Green}Conversion skipped{Colors.Reset}")
            return
    
    # Get conversion parameters
    etc_format = get_etc_format()  # Get ETC format (RGBA8, ETC2, etc)
    error_metric = get_error_metric()  # Get error metric type
    options = get_additional_options()  # Get additional conversion options
    
    # Perform conversion
    success = convert_image_to_ktx(
        str(input_path),
        str(output_path),
        etc_format,
        error_metric,
        options,
        toolpath
    )
    
    # Handle conversion failure
    if not success:
        retry = input(f"\n{Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Green}Retry?  {Colors.Light_Blue}({Colors.Green}y/{Colors.Red}n{Colors.Light_Blue}): {Colors.Reset}").lower()
        retry = check_for_exit(retry)
        if retry == 'y':
            process_single_file_conversion(toolpath)  # Restart process

#______________________________________________________________________________

# Single file conversion processor
# Handles all steps for converting individual image files:
# 1. Input file validation
# 2. Output file handling
# 3. Conversion parameter collection
# 4. Actual conversion execution
def process_folder_conversion(toolpath):
    """Handles batch conversion of all supported images in a folder
    Args:
        toolpath: Path to EtcTool.so binary"""
    while True:
        # Get folder path from user
        input_folder = input(f"\n{Colors.Cyan}• {Colors.Green}[2/5]: {Colors.White}Enter the folder path\n{' ' * 3}{Colors.Green}» ")
        input_folder = check_for_exit(input_folder)  # Check for exit command
        
        # Validate input
        if not input_folder:
            print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] Enter a folder path{Colors.Reset}")
            continue
        
        # Verify folder exists
        input_path = Path(input_folder)
        if input_path.is_dir():
            break
        print(f"{' ' * 9}› {Colors.Red}[ ! ] Error: {Colors.White}{input_folder} {Colors.Red}is not a valid directory!{Colors.Reset}")
    
    # Get conversion parameters
    etc_format = get_etc_format()  # Get compression format
    error_metric = get_error_metric()  # Get quality metric
    options = get_additional_options()  # Get mipmaps/effort settings
    
    # Perform batch conversion
    success = convert_folder(str(input_path), etc_format, error_metric, options, toolpath)
    
    # Handle conversion failure
    if not success:
        retry = input(f"\n{Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Green}Retry?  {Colors.Light_Blue}({Colors.Green}y/{Colors.Red}n{Colors.Light_Blue}): {Colors.Reset}").lower()
        retry = check_for_exit(retry)
        if retry == 'y':
            process_folder_conversion(toolpath)  # Restart process

#______________________________________________________________________________

# Command-line interface processor
# Handles non-interactive conversions via command line arguments:
# 1. Argument parsing
# 2. Settings configuration
# 3. File/folder detection
# 4. Conversion execution
def execute_cli_conversion(args):
    """Handles command-line interface conversion workflow
    Args:
        args: Command line arguments list"""
    try:
        clear_console()  # Clear terminal for clean output
        
        # Verify EtcTool exists
        toolpath = verify_etctool()
        if not toolpath:
            check_for_exit("exit")  # Exit if no EtcTool

        # Default conversion settings
        etc_format = "RGBA8"  # Default format
        error_metric = "rgba"  # Default quality metric
        options = ["-mipmaps", "11", "-effort", "50"]  # Default: max mipmaps, normal effort
        verbose = False  # Verbose logging off by default
        input_path = Path(args[1])  # First arg after script name
        
        # Parse command line arguments
        i = 1  # Start at 1 to skip script name
        
        while i < len(args):
            arg = args[i]
            if arg.startswith('-'):  # Handle options
                if arg == '-mipmaps' and i+1 < len(args):  # Mipmap level setting
                    mipmaps = args[i+1]
                    try:
                        mipmaps_int = int(mipmaps)
                        if mipmaps_int < 0 or mipmaps_int > 11:  # Validate range
                            print(f"{' ' * 2}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Mipmaps value must be {Colors.White}({Colors.Green}0{Colors.White}-{Colors.Green}11{Colors.White})")
                            return
                        options[1] = mipmaps  # Update mipmap setting
                    except ValueError as e:
                        print(f"{' ' * 2}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Invalid mipmaps value")
                        return
                    i += 2  # Skip next arg (value)
                elif arg == '-effort' and i+1 < len(args):  # Compression effort
                    effort = args[i+1]
                    try:
                        effort_int = int(effort)
                        if effort_int < 0 or effort_int > 100:  # Validate range
                            print(f"{' ' * 2}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Effort value must be {Colors.White}({Colors.Green}0{Colors.White}-{Colors.Green}100{Colors.White})")
                            return
                        options[3] = effort  # Update effort setting
                    except ValueError as e:
                        print(f"{' ' * 2}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Invalid effort value")
                        return
                    i += 2  # Skip next arg (value)
                elif arg == '-verbose' and i+1 < len(args):  # Verbose output
                    verbose_arg = args[i+1].lower()
                    if verbose_arg in ('on', 'yes', 'y', 'true', '1'):  # Enable verbose
                        verbose = True
                        options.append("-verbose")  
                    elif verbose_arg in ('off', 'no', 'n', 'false', '0'):  # Disable verbose
                        verbose = False
                        if "-verbose" in options:
                            options.remove("-verbose")
                    else:
                        print(f"{' ' * 9}› {Colors.White}[ {Colors.Red}! {Colors.White}] {Colors.Red}Error: {Colors.White}Invalid verbose value Use {Colors.White}({Colors.Green}y{Colors.White}/{Colors.Red}n{Colors.White})")
                        return
                    i += 2  # Skip next arg (value)
                else:
                    i += 1  # Skip unrecognized flags
            else:
                # This is the input path (non-flag argument)
                input_path = Path(arg)
                i += 1
        
        # Folder conversion mode
        if input_path.is_dir():
            input_folder = str(input_path)
            
            # Display conversion settings
            options_str = ' '.join(options)
            print(f"\n{Colors.Cyan}• {Colors.White}[ {Colors.Light_Blue}Starting Conversion {Colors.White}]{Colors.Reset}")
            print(f"{Colors.Green}╭─────────────────────────────────────────────╮")
            print(f"{Colors.Green}│ {Colors.White}Folder{Colors.Light_Blue}: {Colors.Green}{input_folder.ljust(36)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Format{Colors.Light_Blue}: {Colors.Green}{etc_format.ljust(36)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Metric{Colors.Light_Blue}: {Colors.Green}{error_metric.ljust(36)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Options{Colors.Light_Blue}: {Colors.Green}{options_str.ljust(35)}{Colors.Green}│")
            print(f"{Colors.Green}╰─────────────────────────────────────────────╯")
            
            return convert_folder(input_folder, etc_format, error_metric, options, toolpath)
        
        # Single file conversion mode
        else:
            # Handle missing extensions
            if input_path.is_file():
                input_file = str(input_path)
            else:
                found = False
                for ext in Formats.FORMATS.keys():  # Try known extensions
                    test_path = input_path.with_suffix(ext)
                    if test_path.is_file():
                        input_file = str(test_path)
                        found = True
                        break
                
                if not found:
                    raise ValueError(f"File not found: {input_path}")
            
            # Validate input file
            if not check_file(input_file, 1, 0):
                check_for_exit("exit")
                
            # Set output path
            output_path = input_path.with_suffix('.ktx')
            output_file = str(output_path)
            
            # Validate file format
            file_ext = input_path.suffix.lower().replace('.', '')
            valid_etc_formats = set([fmt[0].lower() for fmt in Formats.FORMATS.values() if isinstance(fmt, (list, tuple))])
            if file_ext not in valid_etc_formats:
                print(f"\n{' ' * 2}› {Colors.Red}[ ! ] Error: {Colors.White}Invalid file format '{Colors.Red}{file_ext}{Colors.White}'. \n{' ' * 4}› Valid formats are: {', '.join(valid_etc_formats)}")
                return
            
            # Display conversion settings
            options_str = ' '.join(options)
            print(f"\n{Colors.Cyan}• {Colors.White}[ {Colors.Light_Blue}Starting Conversion {Colors.White}]{Colors.Reset}")
            print(f"{Colors.Green}╭─────────────────────────────────────────────╮")
            print(f"{Colors.Green}│ {Colors.White}Input File{Colors.Light_Blue}: {Colors.Green}{input_path.name.ljust(30)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Output File{Colors.Light_Blue}: {Colors.Green}{output_path.name.ljust(29)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Format{Colors.Light_Blue}: {Colors.Green}{etc_format.ljust(36)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Metric{Colors.Light_Blue}: {Colors.Green}{error_metric.ljust(36)}{Colors.Green}│")
            print(f"{Colors.Green}│ {Colors.White}Options{Colors.Light_Blue}: {Colors.Green}{options_str.ljust(35)}{Colors.Green}│")
            print(f"{Colors.Green}╰─────────────────────────────────────────────╯{Colors.Reset}")
            
            # Handle existing output file
            if output_path.exists():
                print(f"\n{Colors.Yellow}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Yellow}Output file {Colors.Green}already exists{Colors.Reset}")
                print(f"{Colors.Yellow}╭─────────────────────────────────────────────╮")
                print(f"{Colors.Yellow}│ {Colors.White}File{Colors.Light_Blue}: {Colors.Yellow}{output_path.name.ljust(36)}{Colors.Reset}  {Colors.Yellow}│")
                print(f"{Colors.Yellow}╰─────────────────────────────────────────────╯")
                
                # Prompt for overwrite
                overwrite = input(f"{' ' * 3}{Colors.Yellow}» Overwrite existing file? {Colors.Light_Blue}({Colors.Green}y{Colors.Light_Blue}/{Colors.Red}n{Colors.Light_Blue}): {Colors.Green}").lower()
                overwrite = check_for_exit(overwrite)
                if overwrite != 'y':
                    print(f"\n{Colors.Green}• {Colors.White}[ {Colors.Light_Blue}✓ {Colors.White}]: {Colors.Green}Conversion skipped{Colors.Reset}")
                    return
            
            return convert_image_to_ktx(input_file, output_file, etc_format, error_metric, options, toolpath)
    
    except Exception as e:
        # Error handling
        print(f"\n{Colors.Red}• {Colors.White}[ {Colors.Red}! {Colors.White}]: {Colors.Red}CLI Error:{Colors.Reset}")
        print(f"{Colors.Red}╭─────────────────────────────────────────────╮")
        print(f"{Colors.Red}│ {Colors.White}{str(e).ljust(44)}{Colors.Red}│")
        print(f"{Colors.Red}╰─────────────────────────────────────────────╯{Colors.Reset}")
        return False

#______________________________________________________________________________

def main() -> None:
    """Main entry point for the converter application.
    
    Determines whether to run in CLI or interactive mode based on arguments.
    Handles user interruptions and errors gracefully.
    """
    try:
        # Check if command-line arguments were provided (excluding script name)
        if len(sys.argv) > 1:  
            # Execute CLI conversion with arguments (skip script name)
            execute_cli_conversion(sys.argv[1:])  
        else:  
            # No arguments provided, launch interactive mode
            launch_interactive_converter()
    
    # Catch and display any unexpected errors
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)  # Exit with error code 1


# Standard Python entry point check
if __name__ == "__main__":
    main()