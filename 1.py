import torch

print("PyTorch 版本:", torch.__version__)
print("CUDA 是否可用:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU 名称:", torch.cuda.get_device_name(0))
    print("当前设备 ID:", torch.cuda.current_device())
    print("CUDA 版本:", torch.version.cuda)
    print("GPU 数量:", torch.cuda.device_count())
else:
    print("未检测到可用的 CUDA GPU。")

