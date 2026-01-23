#!/bin/bash
echo "=== Clean Reinstall of Torch ==="

echo "1. Uninstalling everything..."
pip uninstall torch torchvision torchaudio unsloth -y 2>/dev/null || true

echo "2. Cleaning cache..."
rm -rf ~/.cache/torch ~/.cache/pip
find ~/fine_tune_LLM/venv/lib/python3.10/site-packages -name "*torch*" -type d -exec rm -rf {} + 2>/dev/null || true

echo "3. Installing fresh torch 2.3.0..."
pip install torch==2.3.0+cu121 torchvision==0.18.0+cu121 torchaudio==2.3.0+cu121 --index-url https://download.pytorch.org/whl/cu121

echo "4. Verifying torch..."
python3 -c "
import torch
print(f'  torch: {torch.__version__}')
print(f'  CUDA: {torch.cuda.is_available()}')
print(f'  Path: {torch.__file__}')
"

echo "5. Installing unsloth..."
pip install unsloth

echo "6. Testing unsloth import..."
python3 -c "
try:
    from unsloth import FastLanguageModel
    print('  ✅ unsloth imports successfully!')
    
    # Quick test with tiny model
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
