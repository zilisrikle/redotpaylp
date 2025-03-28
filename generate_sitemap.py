import os
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_sitemap(directory):
    # 创建根元素
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # 网站域名
    base_url = 'https://bestcryptocard.xyz'
    
    # 遍历目录下的所有HTML文件
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            # 创建URL元素
            url = ET.SubElement(urlset, 'url')
            
            # 设置loc（网址）
            loc = ET.SubElement(url, 'loc')
            if filename == 'index.html':
                loc.text = base_url
            else:
                loc.text = f'{base_url}/{filename}'
            
            # 设置lastmod（最后修改时间）
            lastmod = ET.SubElement(url, 'lastmod')
            file_path = os.path.join(directory, filename)
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            lastmod.text = mod_time.strftime('%Y-%m-%d')
            
            # 设置changefreq（更新频率）
            changefreq = ET.SubElement(url, 'changefreq')
            if filename == 'index.html':
                changefreq.text = 'weekly'
            else:
                changefreq.text = 'monthly'
            
            # 设置priority（优先级）
            priority = ET.SubElement(url, 'priority')
            if filename == 'index.html':
                priority.text = '1.0'
            else:
                priority.text = '0.8'
    
    # 格式化XML
    xmlstr = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent='    ')
    
    # 保存文件
    with open(os.path.join(directory, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(xmlstr)

if __name__ == '__main__':
    # 获取脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_sitemap(current_dir)
    print('站点地图已更新！')
