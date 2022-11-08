import os
from imageDA import settings
from imageDA.image_dataset import ImageDataset


class OfficeDataset (ImageDataset):
    def __init__(self, img_size, range01, rgb_order, images_dir, dummy=False):
        class_names = []
        names = []
        paths = []
        y = []

        for dir_name in sorted(list(os.listdir(images_dir))):
            cls_dir_path = os.path.join(images_dir, dir_name)
            if os.path.isdir(cls_dir_path):
                cls_i = len(class_names)
                class_names.append(dir_name)

                for file_name in os.listdir(cls_dir_path):
                    file_path = os.path.join(cls_dir_path, file_name)
                    if os.path.isfile(file_path):
                        name = dir_name + '/' + file_name
                        names.append(name)
                        paths.append(os.path.join(cls_dir_path, file_name))
                        y.append(cls_i)

        super(OfficeDataset, self).__init__(img_size, range01, rgb_order, class_names, len(class_names),
                                             names, paths, y, dummy=dummy)


class OfficeAmazonDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('office_amazon')
        super(OfficeAmazonDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)


class OfficeDSLRDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('office_dslr')
        super(OfficeDSLRDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)


class OfficeWebcamDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('office_webcam')
        super(OfficeWebcamDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeAmazon2DsrlDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('amazon_dslr')
        super(OfficeAmazon2DsrlDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeAmazon2WebcamDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('amazon_webcam')
        super(OfficeAmazon2WebcamDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeDslr2AmazonDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('dslr_amazon')
        super(OfficeDslr2AmazonDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeDslr2WebcamDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('dslr_webcam')
        super(OfficeDslr2WebcamDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeWebcam2AmazonDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('webcam_amazon')
        super(OfficeWebcam2AmazonDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)

class OfficeWebcam2DslrDataset (OfficeDataset):
    def __init__(self, img_size, range01=False, rgb_order=False, dummy=False):
        images_dir = settings.get_data_dir('webcam_dslr')
        super(OfficeWebcam2DslrDataset, self).__init__(img_size, range01, rgb_order, images_dir, dummy=dummy)
