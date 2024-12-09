from ultralytics import YOLO

model = YOLO('E:\AntiSpoofAI\models\l_version_1_300.pt')

def main():
    model.train(data='E:\AntiSpoofAI\Dataset\SplitData\data.yaml', epochs=300)


if __name__ == '__main__':
    main()