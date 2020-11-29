


# read single image and plot 16 transformations with matplotlib.pyplot
def plot_16():
    image = plt.imread('images/3 karo.jpg')
    images = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        #imshow(images[0])
        #show()
    data_generator = ImageDataGenerator(rotation_range=90, brightness_range=(0.5, 1.5), shear_range=15.0, zoom_range=[.3, .8])
    data_generator.fit(images)
    image_iterator = data_generator.flow(images)
    plt.figure(figsize=(16,16))
    for i in range(16):
        plt.subplot(4,4,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image_iterator.next()[0].astype('int'))
        print(i)
    plt.show()
#plot_16()