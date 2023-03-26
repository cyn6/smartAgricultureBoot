import torch
from PIL import Image
from skimage import io
import argparse
from torchvision.transforms import transforms
from model import resnet50

parser = argparse.ArgumentParser(description="plant insects and diseases detect")
parser.add_argument('--img_url', type=str, default=None)
parser.add_argument('--type', type=str, default='insect')
args = parser.parse_args()


def preprocess_image(img_path, ):
    # Below code is to show the image
    # sample = io.imread(img_path)
    # io.use_plugin('matplotlib')
    # io.imshow(sample)
    # io.show()

    sample = Image.fromarray(io.imread(img_path)).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    return transform(sample).unsqueeze(0)


def load_model(type, device):
    # 下次模型和参数一起保存
    if type == 'insect':
        model = resnet50(num_classes=102)
        # TODO: absolute model path
        model_params = torch.load('/data/cyn/app/smartAgricultureBoot/plantAPI/ip102_resnet50_checkpoint.pth', map_location=str(device))
    elif type == 'disease':
        model = resnet50(num_classes=42)
        model_params = torch.load('/data/cyn/app/smartAgricultureBoot/plantAPI/mixdisease_resnet50_checkpoint.pth', map_location=str(device))
    model.load_state_dict(model_params)
    model = model.to(device)
    return model


def main():
    ip102_labels = ['rice leaf roller', 'rice leaf caterpillar', 'paddy stem maggot', 'asiatic rice borer',
                    'yellow rice borer', 'rice gall midge', 'Rice Stemfly', 'brown plant hopper',
                    'white backed plant hopper', 'small brown plant hopper', 'rice water weevil', 'rice leafhopper',
                    'grain spreader thrips', 'rice shell pest', 'grub', 'mole cricket', 'wireworm',
                    'white margined moth', 'black cutworm', 'large cutworm', 'yellow cutworm', 'red spider',
                    'corn borer', 'army worm', 'aphids', 'Potosiabre vitarsis', 'peach borer', 'english grain aphid',
                    'green bug', 'bird cherry-oataphid', 'wheat blossom midge', 'penthaleus major',
                    'longlegged spider mite', 'wheat phloeothrips', 'wheat sawfly', 'cerodonta denticornis', 'beet fly',
                    'flea beetle', 'cabbage army worm', 'beet army worm', 'Beet spot flies', 'meadow moth',
                    'beet weevil', 'sericaorient alismots chulsky', 'alfalfa weevil', 'flax budworm',
                    'alfalfa plant bug', 'tarnished plant bug', 'Locustoidea', 'lytta polita', 'legume blister beetle',
                    'blister beetle', 'therioaphis maculata Buckton', 'odontothrips loti', 'Thrips',
                    'alfalfa seed chalcid', 'Pieris canidia', 'Apolygus lucorum', 'Limacodidae', 'Viteus vitifoliae',
                    'Colomerus vitis', 'Brevipoalpus lewisi McGregor', 'oides decempunctata',
                    'Polyphagotars onemus latus', 'Pseudococcus comstocki Kuwana', 'parathrene regalis', 'Ampelophaga',
                    'Lycorma delicatula', 'Xylotrechus', 'Cicadella viridis', 'Miridae', 'Trialeurodes vaporariorum',
                    'Erythroneura apicalis', 'Papilio xuthus', 'Panonchus citri McGregor',
                    'Phyllocoptes oleiverus ashmead', 'Icerya purchasi Maskell', 'Unaspis yanonensis',
                    'Ceroplastes rubens', 'Chrysomphalus aonidum', 'Parlatoria zizyphus Lucus', 'Nipaecoccus vastalor',
                    'Aleurocanthus spiniferus', 'Tetradacus c Bactrocera minax', 'Dacus dorsalis(Hendel)',
                    'Bactrocera tsuneonis', 'Prodenia litura', 'Adristyrannus', 'Phyllocnistis citrella Stainton',
                    'Toxoptera citricidus', 'Toxoptera aurantii', 'Aphis citricola Vander Goot',
                    'Scirtothrips dorsalis Hood', 'Dasineura sp', 'Lawana imitata Melichar',
                    'Salurnis marginella Guerr', 'Deporaus marginatus Pascoe', 'Chlumetia transversa',
                    'Mango flat beak leafhopper', 'Rhytidodera bowrinii white', 'Sternochetus frigidus', 'Cicadellidae']
    mix_disease = ['Apple Aphis spp', 'Apple Eriosoma lanigerum', 'Apple Monillia laxa', 'Apple Venturia inaequalis',
                   'Apple_Alternaria_Boltch', 'Apple_Brown_Spot', 'Apple_Grey_spot', 'Apple_Mosaic',
                   'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                   'Cauliflower_Bacterial spot rot', 'Cauliflower_Black Rot', 'Cauliflower_Disease Free',
                   'Cauliflower_Downy Mildew', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                   'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy', 'Rice_Bacterialblight', 'Rice_Blast', 'Rice_Brownspot', 'Rice_Tungro',
                   'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy', 'Wheat Healthy', 'Wheat Loose Smut', 'Wheat_Crown and Root Rot',
                   'Wheat_Leaf Rust']

    device = torch.device("cpu")  # "cuda:1" if torch.cuda.is_available() else
    # print(device)

    # 输入2个参数
    img_path = args.img_url
    # img_path = '/data/cyn/plant/databank/ip102_v1.1/images/70000.jpg'
    type = args.type  # 'insect'或'disease'

    img = preprocess_image(img_path).to(device)
    model = load_model(type, device)
    model.eval()
    output = model(img)
    output = torch.softmax(output, 1)
    probablility, index = torch.max(output, 1)
    if type == 'insect':
#         print(ip102_labels[index], probablility.item())
        print(ip102_labels[index])
    elif type == 'disease':
#         print(mix_disease[index], probablility.item())
        print(mix_disease[index])


if __name__ == '__main__':
    main()
