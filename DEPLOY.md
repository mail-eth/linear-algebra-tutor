# 🚀 Deploy ke GitHub & Vercel

## Step 1: Push ke GitHub

### Install GitHub CLI (jika belum)
```bash
brew install gh
```

### Login ke GitHub
```bash
gh auth login
```

### Buat Repository & Push
```bash
cd ~/linear-algebra-tutor

# Init git (sudah dilakukan)
git init
git add .
git commit -m "Initial commit - Linear Algebra Tutor"

# Buat repo di GitHub dan push
gh repo create linear-algebra-tutor --public --source=. --push
```

## Step 2: Deploy ke Vercel

### Option A: Via Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel
```

### Option B: Via Vercel Dashboard (Lebih Mudah)
1. Buka https://vercel.com
2. Login dengan GitHub
3. Klik **"New Project"**
4. Import repository `linear-algebra-tutor`
5. Klik **"Deploy"**
6. Selesai! 🎉

## File yang Sudah Dibuat

| File | Fungsi |
|------|--------|
| `vercel.json` | Konfigurasi deployment Vercel |
| `.gitignore` | File yang di-ignore git |

## Setelah Deploy

- GitHub: `https://github.com/YOUR_USERNAME/linear-algebra-tutor`
- Vercel: `https://linear-algebra-tutor.vercel.app`

## Troubleshooting

### Jika Vercel Error
Pastikan `vercel.json` sudah benar dan file `app.py` ada di root.

### Jika Port 5000 Masih Dipake
```bash
# Kill process di port 5000
lsof -ti:5000 | xargs kill -9

# Atau ganti port di app.py
app.run(debug=True, port=8080)
```
