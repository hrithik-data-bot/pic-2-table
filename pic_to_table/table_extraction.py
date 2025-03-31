"""Module for table extraction."""

from transformers import AutoImageProcessor, TableTransformerForObjectDetection
from PIL import Image, ImageDraw
from huggingface_hub import hf_hub_download
import torch

MODEL_STRING = "microsoft/table-transformer-detection"

class DetectTable:
    """Class for detecting tables in an image."""

    def __init__(self, input_image):
        self.input_image = input_image
        self.image_processor = AutoImageProcessor.from_pretrained(MODEL_STRING)
        self.model = TableTransformerForObjectDetection.from_pretrained(MODEL_STRING)

    def detect_table(self):
        """Detects tables in the image and returns bounding boxes."""
        inputs = self.image_processor(images=self.input_image, return_tensors="pt")
        outputs = self.model(**inputs)

        target_sizes = torch.tensor([self.input_image.size[::-1]])
        results = self.image_processor.post_process_object_detection(
            outputs, threshold=0.9, target_sizes=target_sizes
        )[0]

        detected_boxes = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            detected_boxes.append(box)
            print(
                f"Detected {self.model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )

        return detected_boxes

    def visualize_image(self):
        """visualize the detected table"""

        boxes = self.detect_table()
        if len(boxes) == 1:
            draw = ImageDraw.Draw(self.input_image)
            draw.rectangle(boxes[0], outline="red", width=1)
            return self.input_image

if __name__ == "__main__":
    file_path = hf_hub_download(repo_id="nielsr/example-pdf", repo_type="dataset", filename="example_pdf.png")
    image = Image.open(file_path).convert("RGB")
    obj = DetectTable(image)
    obj.visualize_image().save('xyz.png')