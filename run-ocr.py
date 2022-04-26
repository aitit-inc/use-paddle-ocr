import click
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.

@click.command()
@click.argument('img_path', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), default='result.jpg', show_default=True)
def main(img_path: str, output: str):
    ocr = PaddleOCR(use_angle_cls=True, lang='japan') # need to run only once to download and load model into memory
    result = ocr.ocr(img_path, cls=True)
    for line in result:
        print(line)

    # draw result
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]

    # You NEED the font file.
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./PaddleOCR/doc/fonts/japan.ttc')
    im_show = Image.fromarray(im_show)
    im_show.save(output)


if __name__ == '__main__':
    main()
