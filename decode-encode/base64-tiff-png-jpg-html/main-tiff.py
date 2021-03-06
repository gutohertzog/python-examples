
#------------------------------------------------------------------------------
# decode from base64 to tiff
#------------------------------------------------------------------------------

import base64

html = '<img src="data:image/tiff;base64,SUkqAAgAAAASAP4ABAABAAAAAAAAAAABAwABAAAACgAAAAEBAwABAAAACgAAAAIBAwADAAAA5gAAAAMBAwABAAAAsoAAAAYBAwABAAAAAgAAABEBBAABAAAAgAMAABIBCQABAAAAAQAAABUBAwABAAAAAwAAABYBAwABAAAAKAAAABcBBAABAAAAPwAAABoBBQABAAAA7AAAABsBBQABAAAA9AAAABwBAwABAAAAAQAAACgBAwABAAAAAgAAADIBAgAUAAAA/AAAAD0BAwABAAAAAgAAAGmHBAABAAAAEAEAAF4BAAAIAAgACABIAAAAAQAAAEgAAAABAAAAMjAxOTowNzoyMyAyMTozNDoxOQAGAACQBwAEAAAAMDIyMQGRBwAEAAAAAQIDAACgBwAEAAAAMDEwMAGgCQABAAAAAQAAAAKgCQABAAAACgAAAAOgCQABAAAACgAAAAAAAAAGAAMBAwABAAAABgAAABoBCQABAAAASAAAABsBCQABAAAASAAAACgBCQABAAAAAgAAAAECBAABAAAArAEAAAICBAABAAAA1AEAAAAAAAD/2P/gABBKRklGAAEBAAABAAEAAP/bAEMABQMEBAQDBQQEBAUFBQYHDAgHBwcHDwsLCQwRDxISEQ8RERMWHBcTFBoVEREYIRgaHR0fHx8TFyIkIh4kHB4fHv/bAEMBBQUFBwYHDggIDh4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHv/AABEIAAoACgMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABwgJ/8QAIBAAAgICAgMBAQAAAAAAAAAAAgMBBAUGBxEACCETEv/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwBi60fFuU1XB5beI0a3tWVxGMv2RzeECzk77nALXymDn9LIsE4UkEjIrMJWMH/H4hOfJXsNzHq3Iuy6xhd0cnF4jL2qFJbqVawwEpcS1wTWrJjCgRjszIiKfszMzM+Htlu+6at7CbVhdY2/YMHi1NQ5dLHZJ1ZAG2sprThYFAwRsMzKeuyIyKe5mZ80MoVKtCjXo0ayatSsoUoQlcAtQDHQgIx8EYiIiIj5ER4H/9l4nPv//z8DAwMjIyMDKvgPFgeSQCkIGxnABTGl4ArgsnDFyAwi9eKRRXMYhItmL5p34Gpw+QhTI7J2AOTAPvUA">'

data_base64 = html.split('base64,')[1] # remove text before encoded data
data_base64 = data_base64[:-2]         # remove text after encoded data

#data_base64 = 'SUkqAAgAAAASAP4ABAABAAAAAAAAAAABAwABAAAACgAAAAEBAwABAAAACgAAAAIBAwADAAAA5gAAAAMBAwABAAAAsoAAAAYBAwABAAAAAgAAABEBBAABAAAAgAMAABIBCQABAAAAAQAAABUBAwABAAAAAwAAABYBAwABAAAAKAAAABcBBAABAAAAPwAAABoBBQABAAAA7AAAABsBBQABAAAA9AAAABwBAwABAAAAAQAAACgBAwABAAAAAgAAADIBAgAUAAAA/AAAAD0BAwABAAAAAgAAAGmHBAABAAAAEAEAAF4BAAAIAAgACABIAAAAAQAAAEgAAAABAAAAMjAxOTowNzoyMyAyMTozNDoxOQAGAACQBwAEAAAAMDIyMQGRBwAEAAAAAQIDAACgBwAEAAAAMDEwMAGgCQABAAAAAQAAAAKgCQABAAAACgAAAAOgCQABAAAACgAAAAAAAAAGAAMBAwABAAAABgAAABoBCQABAAAASAAAABsBCQABAAAASAAAACgBCQABAAAAAgAAAAECBAABAAAArAEAAAICBAABAAAA1AEAAAAAAAD/2P/gABBKRklGAAEBAAABAAEAAP/bAEMABQMEBAQDBQQEBAUFBQYHDAgHBwcHDwsLCQwRDxISEQ8RERMWHBcTFBoVEREYIRgaHR0fHx8TFyIkIh4kHB4fHv/bAEMBBQUFBwYHDggIDh4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHv/AABEIAAoACgMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABwgJ/8QAIBAAAgICAgMBAQAAAAAAAAAAAgMBBAUGBxEACCETEv/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwBi60fFuU1XB5beI0a3tWVxGMv2RzeECzk77nALXymDn9LIsE4UkEjIrMJWMH/H4hOfJXsNzHq3Iuy6xhd0cnF4jL2qFJbqVawwEpcS1wTWrJjCgRjszIiKfszMzM+Htlu+6at7CbVhdY2/YMHi1NQ5dLHZJ1ZAG2sprThYFAwRsMzKeuyIyKe5mZ80MoVKtCjXo0ayatSsoUoQlcAtQDHQgIx8EYiIiIj5ER4H/9l4nPv//z8DAwMjIyMDKvgPFgeSQCkIGxnABTGl4ArgsnDFyAwi9eKRRXMYhItmL5p34Gpw+QhTI7J2AOTAPvUA'

data_base64 = data_base64.encode()   # convert string to bytes
data = base64.b64decode(data_base64) # decode from base64 (bytes)
open('output-image.tiff', 'wb').write(data) # write bytes to file



#------------------------------------------------------------------------------
# encode tiff to base64 and embed in html
#------------------------------------------------------------------------------

import base64

data = open('image.tiff', 'rb').read() # read bytes from file
data_base64 = base64.b64encode(data)   # encode to base64 (bytes)
data_base64 = data_base64.decode()     # convert bytes to string

print(data_base64)

html = '<img src="data:image/tiff;base64,' + data_base64 + '">' # embed in html
open('output-tiff.html', 'w').write(html)

# browsers don't display tiff so html can show broken image.
# you have to save from page to file and then you can see tiff.
