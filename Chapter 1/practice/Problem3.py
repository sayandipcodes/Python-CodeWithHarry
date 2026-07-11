import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hi I am Sayandip. I am learning Python.")
engine.runAndWait()

#2

# Install via terminal first: pip install pyfiglet
import pyfiglet

# Print in the default font style
banner = pyfiglet.figlet_format("Hello World")
print(banner)

# Print using a specific font style (e.g., 'slant')
slant_banner = pyfiglet.figlet_format("Sayandip Manna", font="slant")
print(slant_banner)