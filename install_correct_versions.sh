#!/bin/bash
echo "=== Installing Correct PyTorch CUDA 12.1 Versions ==="

echo "1. Installing torch 2.5.1 (latest for CUDA 12.1)..."
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121

echo "2. Verifying installation..."
python3 -c "
import torch, torchvision, torchaudio
print(f'  torch:        {torch.__version__}')
print(f'  torchvision:  {torchvision.__version__}')
print(f'  torchaudio:   {torchaudio.__version__}')
print(f'  CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'  GPU: {torch.cuda.get_device_name(0)}')
"

echo "3. Reinstalling unsloth for compatibility..."
pip install unsloth --force-reinstall

echo "4. Testing unsloth..."
python3 -c "
try:
    from unsloth import FastLanguageModel
    print('  ✅ unsloth imports successfully!')
    
    # Test with small model
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name='unsloth/tinyllama-bnb-4bit',
        max_seq_length=128,
        load_in_4bit=True,
    )
    print('  ✅ Model loading works!')
except Exception as e:
    print(f'  ❌ Error: {e}')
"

echo "=== Done ==="
