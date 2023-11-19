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

        self.overlap_images(15)
        self.save_images('5fps')
        self.images_to_video('5fps', '5fps.mp4', 5)

        self.overlap_images(60)
        self.save_images('20fps')
        self.images_to_video('20fps', '20fps.mp4', 20)

    def load_images(self):
        if not os.path.exists(self.directory):
            print(f"Directory '{self.directory}' does not exist.")
            return

        for i in range(90):
            file_path = os.path.join(self.directory, f'frame{i}.jpg')
            
            try:
                image = Image.open(file_path)
                self.frames.append(image)
            except Exception as e:
                print(f"Error loading image '{filename}': {e}")

    def overlap_images(self, resulting_frames):
        self.result = []
        for i in range(len(self.frames)):
            if resulting_frames == 60 and i % 3 == 2:
                continue
            if resulting_frames == 15 and i % 6 != 0:
                continue

            offset = (i * 10, i * 10)

            draw = ImageDraw.Draw(self.frames[i])
            font = ImageFont.truetype("arial.ttf", 40)
            draw.text(offset, "55-3437", font=font, fill="black")

            self.result.append((self.frames[i], i))

    def save_images(self, file_name):
        if not os.path.exists(file_name):
            os.makedirs(file_name)

        for i in range(len(self.result)):
            self.result[i][0].save(f'{file_name}\\frame{self.result[i][1]}.png')

    def images_to_video(self, folder_name, vid_name, fps):
        first_img = self.result[0]
        frame = cv2.imread(os.path.join(folder_name, f"frame0.png"))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(vid_name, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

        for i in range(len(self.result)):
            img_path = os.path.join(f'{folder_name}\\', f'frame{self.result[i][1]}.png')
            img_array = cv2.imread(img_path)
            video.write(img_array)

        cv2.destroyAllWindows()
        video.release()


if __name__ == "__main__":
    a2 = Assignment2('frames\\', '55-3437')
    a2.run()
