import cv2
import argparse
import os
import sys

def main(): 
# 1. 使用 argparse 接收 4 个参数   
    parser = argparse.ArgumentParser(description="OpenCV 图像处理脚本：灰度、模糊、边缘检测")  
    parser.add_argument("input_path", help="输入图片的路径")   		
    parser.add_argument("output_dir", help="输出图片的保存目录")    
    parser.add_argument("canny_low", type=int, help="Canny 边缘检测的低阈值")   
    parser.add_argument("canny_high", type=int, help="Canny 边缘检测的高阈值")    
    args = parser.parse_args()
	  
	# 2. 读取图片并检查是否成功
    img = cv2.imread(args.input_path)  
    if img is None:  
        print(f"错误: 无法读取图片 '{args.input_path}'，请检查文件是否存在或路径是否正确！")
        sys.exit(1) # 以非 0 状态退出
                   
            
	# 3. 确保输出目录存在    
    os.makedirs(args.output_dir, exist_ok=True)
	    
	# 4. 图像处理流程  
	# 转灰度   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
	# 高斯模糊   
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)   
	# Canny 边缘检测
    edges = cv2.Canny(blurred, args.canny_low, args.canny_high)
	   
	# 5. 构造保存路径并保存  
    gray_path = os.path.join(args.output_dir, "gray.jpg")    
    blur_path = os.path.join(args.output_dir, "blur.jpg")   
    edges_path = os.path.join(args.output_dir, "edges.jpg")
	   
    cv2.imwrite(gray_path, gray)   
    cv2.imwrite(blur_path, blurred)    
    cv2.imwrite(edges_path, edges)
	    
	  # 6. 打印保存成功的路径   
    print("图像处理完成！文件已保存至：")    
    print(f"- 灰度图: {gray_path}")   
    print(f"- 模糊图: {blur_path}")    
    print(f"- 边缘图: {edges_path}")
  
if __name__ == "__main__": 
    main()
    