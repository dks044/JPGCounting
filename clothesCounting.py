import os

def count_jpg_in_directory(root_folder):
    counts = {}

    # 모든 폴더들에 대해서
    for foldername, subfolders, filenames in os.walk(root_folder):
        count = sum(1 for filename in filenames if filename.lower().endswith('.jpg'))
        counts[os.path.basename(foldername)] = count
            
    return counts

def save_counts_to_txt(counts, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for folder, count in counts.items():
            f.write(f'"{folder} 폴더에 의상 이미지 파일 {count}개 들어있음!"\n')

if __name__ == "__main__":
    root_folder = 'V:\\임시_개발용\\test1'  # 루트 폴더
    output_file = 'image_counts.txt'  # 결과를 저장할 파일

    counts = count_jpg_in_directory(root_folder)
    save_counts_to_txt(counts, output_file)
