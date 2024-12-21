from PIL import Image

def reduce_image_quality(input_image_path, output_image_path, quality):
    """
    이미지 화질을 줄이는 함수
    :param input_image_path: 입력 이미지 경로
    :param output_image_path: 출력 이미지 경로
    :param quality: 화질 (1부터 100까지, 낮을수록 화질이 낮아짐)
    """
    try:
        with Image.open(input_image_path) as img:
            img.save(output_image_path, "JPEG", quality=quality)
        print(f"화질이 {quality}%로 줄어든 이미지가 저장되었습니다: {output_image_path}")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예제
input_path = "IMG_7698.PNG"  # 원본 이미지 경로
output_path = "example_reduced1.PNG"  # 저장할 이미지 경로
quality = 50  # 화질을 50%로 설정

reduce_image_quality(input_path, output_path, quality)
