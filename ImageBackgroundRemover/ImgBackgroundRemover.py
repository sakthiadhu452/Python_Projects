from rembg import remove
from PIL import Image
source="dog.jpeg";
final="finaloutput.png";

X=Image.open(source);
result=remove(X)
result.save(final)
print("finished");