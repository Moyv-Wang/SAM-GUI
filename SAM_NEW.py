import torch
import cv2
import numpy as np
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor


def extract_embedding(imagePath):
    checkpoint = "D:\\Development\\Python\\segment-anything2\\checkpoints\\sam2.1_hiera_large.pt"
    model_cfg = "D:\\Development\\Python\\segment-anything2\\checkpoints\\configs\\sam2.1\\sam2.1_hiera_l.yaml"
    predictor = SAM2ImagePredictor(build_sam2(model_cfg, checkpoint))

    with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
        image = cv2.imread(imagePath)
        predictor.set_image(image)
    return predictor

def prePredict(pointPrompts, promptLabels, predictor):
    input_point = np.array(pointPrompts)
    input_label = np.array(promptLabels)
    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True,
    )
    sorted_ind = np.argsort(scores)[::-1]
    masks = masks[sorted_ind]
    scores = scores[sorted_ind]
    logits = logits[sorted_ind]
    mask_input = logits[np.argmax(scores), :, :]
    return mask_input


def segment(pointPrompts, promptLabels, predictor):
    mask_input = prePredict(pointPrompts, promptLabels, predictor)
    input_point = np.array(pointPrompts)
    input_label = np.array(promptLabels)
    masks, scores, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        mask_input=mask_input[None, :, :],
        multimask_output=False,
    )
    return masks


    # sam_checkpoint = "D:\\temp_working\\segment-anything\\models\\sam_vit_h_4b8939.pth"
    # model_type = "vit_h"
    # device = "cuda"
    # image = cv2.imread(imagePath)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    # sam.to(device=device)

    # predictor = SamPredictor(sam)

    # predictor.set_image(image)
    # return predictor
