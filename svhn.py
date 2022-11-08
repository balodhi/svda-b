"""Dataset setting and data loader for MNIST."""


import torch
from torchvision import datasets, transforms

import params


def get_svhn(train):
    """Get svhn dataset loader."""
    split = 'train' if train == True else 'test'
    # image pre-processing
    pre_process = transforms.Compose([transforms.ToTensor(),
                                      transforms.Normalize(
                                          mean=(params.dataset_mean),
                                          std=(params.dataset_std))])

    # dataset and data loader
    svhn_dataset = datasets.SVHN(root=params.data_root,
                                   split=split,
                                   transform=pre_process,
                                   download=True)

    svhn_data_loader = torch.utils.data.DataLoader(
        dataset=svhn_dataset,
        batch_size=params.batch_size,
        shuffle=True)

    return svhn_data_loader

if __name__ == '__main__':
    data = get_svhn(train=True)

    for image,label in data:
        print(image.shape)
        break
