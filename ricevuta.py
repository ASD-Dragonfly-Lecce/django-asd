from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap

def hello(c):
    width, height = letter

    t = c.beginText()
    t.setFont('Helvetica', 10)
    # t.setCharSpace(3)
    t.setTextOrigin(width/20, height-50)

    text =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\n\nMaecenas sem tellus, auctor eget mauris et, consequat vulputate ligula. Proin dictum, mi ac fermentum vulputate, eros est iaculis tellus, sed tempus ex ligula vitae sem. Praesent fringilla mollis suscipit. Donec ut urna vel felis ultricies condimentum. Etiam commodo posuere nibh, sit amet congue dolor ullamcorper a. Nulla laoreet condimentum tortor, non lacinia ipsum cursus dignissim. Quisque pellentesque urna vel sodales consectetur. Nulla facilisi. Nunc sodales fringilla est sit amet suscipit. Nam nec quam ac nisi rutrum faucibus sed vel elit. Nullam rhoncus gravida lorem, eget scelerisque orci tincidunt eget. Aliquam faucibus leo eu libero interdum venenatis. Donec ultrices, tellus nec finibus rhoncus, elit leo varius dui, ac consequat purus ipsum eu nisl. Morbi ac pellentesque nibh, at vehicula sapien. Etiam convallis nisi augue, at blandit enim blandit rhoncus. Proin vestibulum volutpat sollicitudin. Quisque orci odio, vestibulum at urna non, eleifend luctus neque. Curabitur congue, ligula sed sodales lobortis, augue metus tristique eros, at venenatis lorem arcu et risus."


    wrapped_text = "\n".join(wrap(text, 80)) # 80 is line width

    t.textLines(wrapped_text)
    c.drawText(t)

c = canvas.Canvas("hello.pdf", pagesize=letter)
hello(c)
c.showPage()
c.save()

# https://docs.djangoproject.com/en/5.1/topics/templates/