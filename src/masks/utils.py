# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import torch


def apply_masks(x, masks, concat=True):
    """
    :param x: tensor of shape [B (batch-size), N (num-patches), D (feature-dim)]
    :param masks: list of tensors of shape [B, K] containing indices of K patches in [N] to keep
    """
    all_x = []
    for m in masks:
        print("@@@@@@@@@@")
        print(f'mask shape is: {m.shape}')
        print(f'x shape: {x.shape}')
        mask_keep = m.unsqueeze(-1).repeat(1, 1, x.size(-1))
        print(f'mask_keep shape: {mask_keep.shape}')
        print("@@@@@@@@@@")
        all_x += [torch.gather(x, dim=1, index=mask_keep)]
    if not concat:
        return all_x

    return torch.cat(all_x, dim=0)

# modal == 1: vision
# modal == 0: audio 
def av_apply_masks(x, masks, modal=1, concat=True):
    """
    :param x: tensor of shape [B (batch-size), N (num-patches), D (feature-dim)]
    :param masks: list of tensors of shape [B, K] containing indices of K patches in [N] to keep
    """
    all_x = []
    for m in masks:
        print("@@@@@@@@@@")
        print(f'mask shape is: {m.shape}')
        print(f'x shape: {x.shape}')
        mask_keep = m.unsqueeze(-1).repeat(1, 1, x.size(-1))
        print(f'mask_keep shape: {mask_keep.shape}')
        print("@@@@@@@@@@")
        if modal == 1:
            all_x += [torch.gather(x, dim=1, index=mask_keep)]
        else:
            all_x += [torch.gather(x, dim=0, index=mask_keep)]

    if not concat:
        return all_x

    return torch.cat(all_x, dim=0)
