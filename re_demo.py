from lxml import html

# 假设html_content是你的HTML内容
html_content = '''
<td id="tiktokDescEditorBox" class="validformOut">
    <div>
        <input id="saveDescriptionEditorDataIpt" type="hidden" value="&lt;p&gt;Fulfilling Our Social Responsibility: Over the past 2 years, we've collaborated with ClimatePartner to neutralize our carbon footprint. Additionally, for every 10 bottles sold, we're committed to donating 1 tree to Onetreeplanted, contributing to a greener and more vibrant world. Embrace a healthier lifestyle by joining us on this tree-mendous journey towards sustainable hydration&lt;/p&gt;&lt;p&gt;Hydration Reminder Companion: Stay healthy effortlessly with our motivational water bottle. Featuring inspiring quotes and convenient time markings, it keeps you on track for optimal hydration all day long&lt;/p&gt;&lt;p&gt;Safe and Sustainable: Crafted from food-grade, eco-friendly tritan plastic, our sports water bottle is 100% BPA-free and non-toxic. Make a positive impact on your health and the environment by choosing this reusable alternative to plastic bottles&lt;/p&gt;&lt;p&gt;Thoughtful, Durable Design: Designed with your convenience in mind, the Sahara Sailor water bottle boasts an ergonomic shape, sturdy wrist strap, and a distinctive reflective frosted shell. Its 360° leakproof construction ensures hassle-free portability, while the flip cover's safety lock prevents accidental spills. A cleaning brush simplifies maintenance&lt;/p&gt;&lt;p&gt;Effortless Drinking: Experience easy, one-handed hydration with the splash-proof top and intuitive button release. The lid's air holes facilitate swift water flow, and the soft silicone nozzle enables spill-proof sips and rapid gulps, making it ideal for various activities like the gym, camping, or work&lt;/p&gt;&lt;p&gt;Fulfilling Our Social Responsibility: Over the past 2 years, we've collaborated with ClimatePartner to neutralize our carbon footprint. Additionally, for every 10 bottles sold, we're committed to donating 1 tree to Onetreeplanted, contributing to a greener and more vibrant world. Embrace a healthier lifestyle by joining us on this tree-mendous journey towards sustainable hydration Hydration Reminder Companion: Stay healthy effortlessly with our motivational water bottle. Featuring inspiring quotes and convenient time markings, it keeps you on track for optimal hydration all day long Safe and Sustainable: Crafted from food-grade, eco-friendly tritan plastic, our sports water bottle is 100% BPA-free and non-toxic. Make a positive impact on your health and the environment by choosing this reusable alternative to plastic bottles Thoughtful, Durable Design: Designed with your convenience in mind, the Sahara Sailor water bottle boasts an ergonomic shape, sturdy wrist strap, and a distinctive reflective frosted shell. Its 360° leakproof construction ensures hassle-free portability, while the flip cover's safety lock prevents accidental spills. A cleaning brush simplifies maintenance Effortless Drinking: Experience easy, one-handed hydration with the splash-proof top and intuitive button release. The lid's air holes facilitate swift water flow, and the soft silicone nozzle enables spill-proof sips and rapid gulps, making it ideal for various activities like the gym, camping, or work&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;Product Description&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;Sahara Sailor Motivational Water Bottle Three Sizes Available&lt;/p&gt;&lt;p&gt;Previous page&lt;/p&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/dcdf5bde-fed8-4e34-a3dc-32f1f6ae4bf5.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;Ideal for your busy lifestyles&lt;/p&gt;&lt;p&gt;Developed to be carried anywhere&lt;/p&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/cc0f9b50-9313-4ad7-b768-1d0839d89ce1.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;Ideal for your busy lifestyles&lt;/p&gt;&lt;p&gt;Developed to be carried anywhere&lt;/p&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/5b19791e-616b-4531-b3c5-10a2e9085a4e.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;Ideal for your busy lifestyles&lt;/p&gt;&lt;p&gt;Developed to be carried anywhere&lt;/p&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/3b29a7a5-d733-4dda-bee5-9074f9bf0b9c.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;Ideal for your busy lifestyles&lt;/p&gt;&lt;p&gt;Developed to be carried anywhere&lt;/p&gt;&lt;p&gt;Next page&lt;/p&gt;&lt;p&gt;1Working&lt;/p&gt;&lt;p&gt;2Yoga&lt;/p&gt;&lt;p&gt;3Exercising&lt;/p&gt;&lt;p&gt;4Traveling&lt;/p&gt;&lt;p&gt;Thoughtful Features Bring a Better Use Experience&lt;/p&gt;&lt;img src=&quot;https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/db41a64a-2f65-460e-92d0-3b9765c28a07.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;Join the Trend and Hydrate&lt;/p&gt;&lt;p&gt;Previous page&lt;/p&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/139aaf5b-13d2-44ab-a142-a793f3f6a1e2.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/8d20ef79-5f16-4274-bbd0-14ad6ebdf3c5.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/a5d170d0-24ac-417f-b7db-b7d730ce9f53.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/a80555cb-8104-4ead-a82b-baf718bc2d96.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;Next page&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;Reusable Water Bottles to Reduce Single-Use Plastic Consumption&lt;/p&gt;&lt;img src=&quot;https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/8fa5f9fb-34b7-4624-92aa-9a51d89b7e87.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;Our Social Responsibility&lt;/p&gt;&lt;img src=&quot;https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/grey-pixel.gif&quot;&gt;&lt;img src=&quot;https://m.media-amazon.com/images/S/aplus-media-library-service-media/01671be5-11af-473f-b4e0-fa6c9f2ff095.__CR0,0,1464,600_PT0_SX1464_V1___.jpg&quot;&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;&lt;p&gt;&amp;nbsp;&lt;/p&gt;"/>
        <textarea id="description" name="content" style="width: 100%; height: 100%; visibility: hidden; display: none;"/>
        <div id="cke_description" class="cke_3 cke cke_reset cke_chrome cke_editor_description cke_ltr cke_browser_webkit cke_browser_quirks" dir="ltr" lang="zh-cn" role="application" aria-labelledby="cke_description_arialbl">
            <span id="cke_description_arialbl" class="cke_voice_label">所见即所得编辑器, description</span>
            <div class="cke_inner cke_reset" role="presentation">
                <span id="cke_3_top" class="cke_top cke_reset_all" role="presentation" style="height: auto; user-select: none;">
                    <span id="cke_12" class="cke_voice_label">工具栏</span>
                    <span id="cke_3_toolbox" class="cke_toolbox" role="group" aria-labelledby="cke_12" onmousedown="return false;">
                        <span id="cke_15" class="cke_toolbar" role="toolbar">
                            <span class="cke_toolbar_start"/>
                            <span class="cke_toolgroup" role="presentation">
                                <a id="cke_16" class="cke_button cke_button__source cke_button_off" href="javascript:void('源码')" title="源码" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_16_label" aria-describedby="cke_16_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(2,event);" onfocus="return CKEDITOR.tools.callFunction(3,event);" onclick="CKEDITOR.tools.callFunction(4,this);return false;">
                                    <span class="cke_button_icon cke_button__source_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -1848px;background-size:auto;"> </span>
                                    <span id="cke_16_label" class="cke_button_label cke_button__source_label" aria-hidden="false">源码</span>
                                    <span id="cke_16_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                                <a id="cke_17" class="cke_button cke_button__maximize cke_button_off" href="javascript:void('全屏')" title="全屏" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_17_label" aria-describedby="cke_17_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(5,event);" onfocus="return CKEDITOR.tools.callFunction(6,event);" onclick="CKEDITOR.tools.callFunction(7,this);return false;">
                                    <span class="cke_button_icon cke_button__maximize_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -1416px;background-size:auto;"> </span>
                                    <span id="cke_17_label" class="cke_button_label cke_button__maximize_label" aria-hidden="false">全屏</span>
                                    <span id="cke_17_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                                <span class="cke_toolbar_separator" role="separator"/>
                                <a id="cke_18" class="cke_button cke_button__bold cke_button_off" href="javascript:void('加粗')" title="加粗 (Ctrl+B)" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_18_label" aria-describedby="cke_18_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(8,event);" onfocus="return CKEDITOR.tools.callFunction(9,event);" onclick="CKEDITOR.tools.callFunction(10,this);return false;">
                                    <span class="cke_button_icon cke_button__bold_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -24px;background-size:auto;"> </span>
                                    <span id="cke_18_label" class="cke_button_label cke_button__bold_label" aria-hidden="false">加粗</span>
                                    <span id="cke_18_description" class="cke_button_label" aria-hidden="false">快捷键 Ctrl+B</span>
                                </a>
                                <a id="cke_19" class="cke_button cke_button__italic cke_button_off" href="javascript:void('倾斜')" title="倾斜 (Ctrl+I)" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_19_label" aria-describedby="cke_19_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(11,event);" onfocus="return CKEDITOR.tools.callFunction(12,event);" onclick="CKEDITOR.tools.callFunction(13,this);return false;">
                                    <span class="cke_button_icon cke_button__italic_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -48px;background-size:auto;"> </span>
                                    <span id="cke_19_label" class="cke_button_label cke_button__italic_label" aria-hidden="false">倾斜</span>
                                    <span id="cke_19_description" class="cke_button_label" aria-hidden="false">快捷键 Ctrl+I</span>
                                </a>
                                <a id="cke_20" class="cke_button cke_button__underline cke_button_off" href="javascript:void('下划线')" title="下划线 (Ctrl+U)" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_20_label" aria-describedby="cke_20_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(14,event);" onfocus="return CKEDITOR.tools.callFunction(15,event);" onclick="CKEDITOR.tools.callFunction(16,this);return false;">
                                    <span class="cke_button_icon cke_button__underline_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -144px;background-size:auto;"> </span>
                                    <span id="cke_20_label" class="cke_button_label cke_button__underline_label" aria-hidden="false">下划线</span>
                                    <span id="cke_20_description" class="cke_button_label" aria-hidden="false">快捷键 Ctrl+U</span>
                                </a>
                            </span>
                            <span class="cke_toolbar_end"/>
                        </span>
                        <span id="cke_21" class="cke_toolbar" role="toolbar">
                            <span class="cke_toolbar_start"/>
                            <span class="cke_toolgroup" role="presentation">
                                <a id="cke_22" class="cke_button cke_button__bulletedlist cke_button_off" href="javascript:void('项目列表')" title="项目列表" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_22_label" aria-describedby="cke_22_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(17,event);" onfocus="return CKEDITOR.tools.callFunction(18,event);" onclick="CKEDITOR.tools.callFunction(19,this);return false;">
                                    <span class="cke_button_icon cke_button__bulletedlist_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -1344px;background-size:auto;"> </span>
                                    <span id="cke_22_label" class="cke_button_label cke_button__bulletedlist_label" aria-hidden="false">项目列表</span>
                                    <span id="cke_22_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                                <a id="cke_23" class="cke_button cke_button__numberedlist cke_button_off" href="javascript:void('编号列表')" title="编号列表" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_23_label" aria-describedby="cke_23_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(20,event);" onfocus="return CKEDITOR.tools.callFunction(21,event);" onclick="CKEDITOR.tools.callFunction(22,this);return false;">
                                    <span class="cke_button_icon cke_button__numberedlist_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -1392px;background-size:auto;"> </span>
                                    <span id="cke_23_label" class="cke_button_label cke_button__numberedlist_label" aria-hidden="false">编号列表</span>
                                    <span id="cke_23_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                            </span>
                            <span class="cke_toolbar_end"/>
                        </span>
                        <span id="cke_24" class="cke_toolbar" role="toolbar">
                            <span class="cke_toolbar_start"/>
                            <span class="cke_toolgroup" role="presentation">
                                <a id="cke_25" class="cke_button cke_button__newpage cke_button_off" href="javascript:void('清空')" title="清空" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_25_label" aria-describedby="cke_25_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(23,event);" onfocus="return CKEDITOR.tools.callFunction(24,event);" onclick="CKEDITOR.tools.callFunction(25,this);return false;">
                                    <span class="cke_button_icon cke_button__newpage_icon" style="background-image:url('https://www.dianxiaomi.com/static/js/plugin/editor/plugins/icons.png?t=H0CG.18');background-position:0 -1464px;background-size:auto;"> </span>
                                    <span id="cke_25_label" class="cke_button_label cke_button__newpage_label" aria-hidden="false">清空</span>
                                    <span id="cke_25_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                            </span>
                            <span class="cke_toolbar_end"/>
                        </span>
                        <span id="cke_26" class="cke_toolbar cke_toolbar_last" role="toolbar">
                            <span class="cke_toolbar_start"/>
                            <span id="cke_13" class="cke_combo cke_combo__imgdropdownlist cke_format cke_combo_off" role="presentation">
                                <span id="cke_13_label" class="cke_combo_label">选择图片</span>
                                <a class="cke_combo_button" title="选择图片" tabindex="-1" href="javascript:void('选择图片')" hidefocus="true" role="button" aria-labelledby="cke_13_label" aria-haspopup="true" onkeydown="return CKEDITOR.tools.callFunction(27,event,this);" onfocus="return CKEDITOR.tools.callFunction(28,event);" onclick="CKEDITOR.tools.callFunction(26,this);return false;">
                                    <span id="cke_13_text" class="cke_combo_text cke_combo_inlinelabel">选择图片</span>
                                    <span class="cke_combo_open">
                                        <span class="cke_combo_arrow"/>
                                    </span>
                                </a>
                            </span>
                            <span id="cke_14" class="cke_combo cke_combo__batcheditimgdropdownlist cke_format cke_combo_off" role="presentation">
                                <span id="cke_14_label" class="cke_combo_label">批量编辑图片</span>
                                <a class="cke_combo_button" title="批量编辑图片" tabindex="-1" href="javascript:void('批量编辑图片')" hidefocus="true" role="button" aria-labelledby="cke_14_label" aria-haspopup="true" onkeydown="return CKEDITOR.tools.callFunction(30,event,this);" onfocus="return CKEDITOR.tools.callFunction(31,event);" onclick="CKEDITOR.tools.callFunction(29,this);return false;">
                                    <span id="cke_14_text" class="cke_combo_text cke_combo_inlinelabel">批量编辑图片</span>
                                    <span class="cke_combo_open">
                                        <span class="cke_combo_arrow"/>
                                    </span>
                                </a>
                            </span>
                            <span class="cke_toolgroup" role="presentation">
                                <a id="cke_27" class="cke_button cke_button__chatgptplugin cke_button_off" href="javascript:void('AI生成')" title="AI生成" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_27_label" aria-describedby="cke_27_description" aria-haspopup="false" onkeydown="return CKEDITOR.tools.callFunction(32,event);" onfocus="return CKEDITOR.tools.callFunction(33,event);" onclick="CKEDITOR.tools.callFunction(34,this);return false;">
                                    <span class="cke_button_icon cke_button__chatgptplugin_icon" style="background-image:url('/static/img/chatGPT/logo.png?v=1&amp;t=H0CG.18');background-position:0 undefinedpx;background-size:16px;"> </span>
                                    <span id="cke_27_label" class="cke_button_label cke_button__chatgptplugin_label" aria-hidden="false">AI生成</span>
                                    <span id="cke_27_description" class="cke_button_label" aria-hidden="false"/>
                                </a>
                            </span>
                            <span class="cke_toolbar_end"/>
                        </span>
                    </span>
                </span>
                <div id="cke_3_contents" class="cke_contents cke_reset" role="presentation" style="height: 300px;">
                    <span id="cke_31" class="cke_voice_label">按 ALT+0 获得帮助</span>
                    <iframe src="" frameborder="0" class="cke_wysiwyg_frame cke_reset" style="width: 100%; height: 100%;" title="所见即所得编辑器, description" aria-describedby="cke_31" tabindex="0" allowtransparency="true"/>
                </div>
                <span id="cke_3_bottom" class="cke_bottom cke_reset_all" role="presentation" style="user-select: none;">
                    <span id="cke_3_resizer" class="cke_resizer cke_resizer_vertical cke_resizer_ltr" title="拖拽以改变大小" onmousedown="CKEDITOR.tools.callFunction(0, event)">◢</span>
                    <div class="cke_wordcount" style="" title="统计">
                        <span id="cke_wordcount_description" class="cke_path_item">总字符数： 10233</span>
                    </div>
                </span>
            </div>
        </div>
        <div id="cacheDiv" style="display:none;"/>
        <div class="editorImgNumBox f-right w-full m-top10" data-state="0">
            <a href="javascript:" class="fl" onclick="IMG_TESTING.editorProblemImg('tiktok', '#cke_description')">问题图片检测</a>
            <div class="imgNum">您已添加30张图片，TikTok限制最多添加30张</div>
            <div class="imgErr f-red m-top10"/>
        </div>
    </div>
</td>
'''

# 解析HTML
htmls = html.fromstring(html_content)

data_info = {
    'description': html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).text_content(),
    'image_urls': html.fromstring(htmls.xpath('//input[@id="saveDescriptionEditorDataIpt"]/@value')[0]).xpath('//img/@src')
}

print(data_info)
