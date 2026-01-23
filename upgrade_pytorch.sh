#!/bin/bash
echo "=== Upgrading to Compatible Versions ==="

echo "1. Upgrading torch to 2.5.1 (compatible with CUDA 12.1)..."
pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121

echo "2. Upgrading triton..."
pip install triton==3.5.1

echo "3. Verifying versions..."
python3 -c "
import torch, torchvision, torchaudio
import triton
print(f'  torch: {torch.__version__}')
print(f'  torchvision: {torchvision.__version__}')
print(f'  torchaudio: {torchaudio.__version__}')
print(f'  triton: {triton.__version__}')
print(f'  CUDA: {torch.cuda.is_available()}')
"

echo "4. Reinstalling unsloth..."
pip install unsloth --force-reinstall

echo "5. Testing unsloth..."
python3 -c "
try:
    from unsloth import FastLanguageModel
    print('  ✅ unsloth imports successfully!')
    
    # Quick test
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name='unsloth/tinyllama-bnb-4bit',
        max_seq_length=128,
        load_in_4bit=True,
    )
    print('  ✅ Model loading works!')
except Exception as e:
    print(f'  ❌ Error: {e}')
    import traceback
    traceback.print_exc()
"

echo "=== Done ==="
