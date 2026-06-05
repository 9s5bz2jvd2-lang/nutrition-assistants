# 安装指南

## 方式1：一键安装（推荐）

### Linux/Mac

```bash
curl -fsSL https://raw.githubusercontent.com/yourusername/glucose-revolution-skill/main/quick-install.sh | bash
```

### Windows

```powershell
# 下载安装脚本
Invoke-WebRequest -Uri "https://github.com/yourusername/glucose-revolution-skill/releases/latest/download/glucose-revolution-skill.zip" -OutFile "skill.zip"

# 解压到 WorkBuddy 目录
Expand-Archive -Path "skill.zip" -DestinationPath "$env:USERPROFILE\.workbuddy\skills\custom\"
```

## 方式2：手动安装

### 从 Release 下载

1. 访问 [Releases 页面](https://github.com/yourusername/glucose-revolution-skill/releases)
2. 下载最新的 `glucose-revolution-skill.zip`
3. 解压到对应目录

### 安装到 WorkBuddy

```bash
# 解压到 WorkBuddy skills 目录
unzip glucose-revolution-skill.zip -d ~/.workbuddy/skills/custom/glucose-revolution-skill
```

### 安装到 灵台 TUI

```bash
# 解压到灵台 custom 目录
unzip glucose-revolution-skill.zip -d ~/.lingtai/custom/glucose-revolution-skill
```

## 方式3：Git 克隆

```bash
git clone https://github.com/yourusername/glucose-revolution-skill.git

cd glucose-revolution-skill
bash install.sh
```

## 验证安装

安装完成后，重启你的 AI 助手，然后输入：

```
控糖
```

如果 Skill 被正确加载，你会看到控糖导师的回应。

## 目录结构

安装后，你的目录结构应该如下：

```
~/.workbuddy/skills/custom/
└── glucose-revolution-skill/
    ├── skill.yaml
    ├── system_prompt.md
    └── ...
```

## 卸载

```bash
rm -rf ~/.workbuddy/skills/custom/glucose-revolution-skill
```

## 故障排除

### Skill 没有触发

1. 检查安装路径是否正确
2. 确认文件权限：`chmod -R 755 ~/.workbuddy/skills/custom/glucose-revolution-skill`
3. 重启 AI 助手

### 触发关键词无效

尝试以下任意关键词：
- "控糖"
- "血糖"
- "饮食顺序"
- "血糖峰值"

### 联系支持

如有问题，请提交 [Issue](https://github.com/yourusername/glucose-revolution-skill/issues)
