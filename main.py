from cyclegan import *
from data_loader import *
from PIL import Image

row_size = 400
col_size = 400

if sys.argv[1] == '-t':
    gan = CycleGAN(row_size, col_size, 3)
    gan.train(epochs=200, batch_size=1, sample_interval=200)
elif sys.argv[1] == '-p':
    if sys.argv[2] != '':
        input_path = sys.argv[2]
        # img = Image.open(input_path)
        # img = img.resize((col_size, row_size), Image.ANTIALIAS)
        # img = np.array(img)
        # img = np.array([img])
        loader = DataLoader('', (row_size, col_size))
        img = loader.load_img('./test_input.jpg')
        gan = load_model('./saved_models/fill_color.h5')
        output_img = gan.predict(img)
        output_img = (output_img + 1) / 2 * 255
        output_img = output_img.astype(np.uint8)
        pic = output_img[0,:,:,:]
        plt.imsave('./test_out.png', arr=pic)
        print('Done!')
    else:
        print('Invalid input image path!')
else:
    print('Unknown command!')
