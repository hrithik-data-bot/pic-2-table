"""Module for table structure recognition."""


from transformers import AutoImageProcessor, TableTransformerForObjectDetection
from PIL import ImageDraw
import torch

MODEL_STRUCTURE = "microsoft/table-transformer-structure-recognition"

class RecognizeTableStructure:
    """Class for recognizing the table structure in an image."""

    def __init__(self, input_image):
        self.input_image = input_image
        self.image_processor = AutoImageProcessor.from_pretrained(MODEL_STRUCTURE)
        self.model = TableTransformerForObjectDetection.from_pretrained(MODEL_STRUCTURE)

    def recognize_structure(self):
        """Recognizes the table structure and returns cell coordinates."""
        inputs = self.image_processor(images=self.input_image, return_tensors="pt")
        outputs = self.model(**inputs)

        target_sizes = torch.tensor([self.input_image.size[::-1]])
        results = self.image_processor.post_process_object_detection(
            outputs, threshold=0.9, target_sizes=target_sizes
        )[0]

        detected_cells = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            detected_cells.append((self.model.config.id2label[label.item()], box))
            print(
                f"Detected {self.model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )

        return detected_cells

    def visualize_structure(self):
        """Visualizes the recognized table structure by drawing bounding boxes around cells."""
        cells = self.recognize_structure()
        if cells:
            draw = ImageDraw.Draw(self.input_image)
            for label, box in cells:
                color = "blue" if label == "cell" else "green"
                draw.rectangle(box, outline=color, width=2)
            return self.input_image
        else:
            print("No table structure detected.")
            return self.input_image
