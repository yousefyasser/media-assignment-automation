from PIL import Image, ImageDraw, ImageFont
import cv2
import os

class Assignment2:
    def __init__(self, directory, Id):
        self.frames = []
        self.result = []
        self.directory = directory
        self.id = Id

    def run(self):
        self.load_images()
        self.overlap_images()
        self.save_images()
        self.images_to_video()

    def load_images(self):
        if not os.path.exists(self.directory):
            print(f"Directory '{self.directory}' does not exist.")
            return

        for filename in os.listdir(self.directory):
            
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(self.directory, filename)
                
                try:
                    image = Image.open(file_path)
                    self.frames.append(image)
                except Exception as e:
                    print(f"Error loading image '{filename}': {e}")

    def overlap_images(self):
        
        for i in range(0, len(self.frames)):
            if i % 3 == 2:
                continue 

            offset = (i * 10, i * 10)

            draw = ImageDraw.Draw(self.frames[i])
            font = ImageFont.truetype("arial.ttf", 40)
            draw.text(offset, "55-3437", font=font, fill="black")

            self.result.append(self.frames[i])

    def save_images(self):
        if not os.path.exists('result'):
            os.makedirs('result')

        for i in range(len(self.result)):
            self.result[i].save(f'result\\{i}.png')

    def images_to_video(self, fps=20):
        first_img = self.result[0]
        frame = cv2.imread(os.path.join('result\\', f"{0}.png"))
        height, width, layers = frame.shape

        video = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

        for i in range(len(self.result)):
            img_path = os.path.join('result\\', f"{i}.png")
            img_array = cv2.imread(img_path)
            video.write(img_array)

        cv2.destroyAllWindows()
        video.release()


if __name__ == "__main__":
    a2 = Assignment2('frames\\', '55-3437')
    a2.run()
