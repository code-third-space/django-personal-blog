(function($) {
    $(document).ready(function() {
        var subcategoryMap = {
            0: [  // 技术类
                [0, "编程开发"],
                [1, "人工智能"],
                [2, "数据科学"],
                [3, "网络安全"],
                [4, "云计算"],
                [5, "区块链"],
                [6, "物联网"],
                [7, "移动开发"],
                [8, "前端技术"],
                [9, "后端技术"]
            ],
            1: [  // 资讯类
                [0, "国内新闻"],
                [1, "国际新闻"],
                [2, "科技动态"],
                [3, "社会热点"],
                [4, "政治时事"],
                [5, "文化教育"]
            ],
            2: [  // 财经类
                [0, "股票市场"],
                [1, "基金投资"],
                [2, "外汇交易"],
                [3, "经济分析"],
                [4, "财经政策"],
                [5, "企业财报"]
            ],
            3: [  // 阅读类
                [0, "文学作品"],
                [1, "历史读物"],
                [2, "科普书籍"],
                [3, "哲学思想"],
                [4, "心理学"],
                [5, "经管励志"]
            ],
            4: [  // 风景类
                [0, "自然风光"],
                [1, "城市景观"],
                [2, "历史古迹"],
                [3, "人文景观"],
                [4, "旅游攻略"],
                [5, "摄影技巧"]
            ],
            5: [  // 物品类
                [0, "数码产品"],
                [1, "家居用品"],
                [2, "服饰穿搭"],
                [3, "美食烹饪"],
                [4, "汽车评测"],
                [5, "收藏品"]
            ]
        };

        function updateSubcategories() {
            var blogType = $('#id_blog_type').val();
            var $subcategory = $('#id_subcategory');
            
            // 清空现有选项
            $subcategory.empty();
            
            // 添加默认选项
            $subcategory.append($('<option>', {
                value: '',
                text: '---------'
            }));
            
            // 如果选择了博客类型，添加对应的二级分类
            if (blogType !== '' && subcategoryMap[blogType]) {
                subcategoryMap[blogType].forEach(function(item) {
                    $subcategory.append($('<option>', {
                        value: item[0],
                        text: item[1]
                    }));
                });
            }
        }

        // 监听博客类型的变化
        $('#id_blog_type').change(updateSubcategories);
        
        // 页面加载时初始化
        updateSubcategories();
    });
})(django.jQuery); 