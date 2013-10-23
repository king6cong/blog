Title: 嵌入优酷html5视频
Category: Magic tools
Slug: my-super-post
Date: 2013-10-23 10:20
Tags: javascript

视频是一种非常有效的表达方式：

1. 在博客上用视频表达一些观点
2. 在产品页提供demo视频，让用户更快了解产品，比如 [Bungeer视频app][1]
    
虽然可以将视频放在自己的server上，但对于非专攻视频的站点:

1. 访问速度难以保证
2. 流量可能也是问题

优酷的在这些方面做的很好，将视频放到优酷是不错的解决方案。

但是优酷提供的嵌入方式有些不理想的地方：

1. 桌面浏览器默认使用flash播放，在Mac，Linux等平台上体验不好。
2. 短视频的广告较长。视频网站运营费用很高，有广告是非常能让人理解的。但对于短视频，个人认为，可以考虑缩短广告时间。如果广告比视频还长，的确比较尴尬。

在实际使用中，如果官网高端大气上档次，demo视频却以广告开场，也挺雷人的。

在开发Bungeer视频的过程中，提取了这样一个工具，能将优酷视频以html5方式嵌入自己的页面中，播放器使用的是 [video.js][2]

#### how to use：

1.优酷视频url，以及封面（可选），可以嵌入多个视频

    <div class="bungeer_video_html5" href="http://v.youku.com/v_show/id_XNjEyODk1MzM2.html" poster="http://www.bungeer.com/static/img/web_hi_res_512.png"></div>

2.最后引入jQuery以及video_html5.js

    <script>window.jQuery || document.write('<script src="http://codeorigin.jquery.com/jquery-1.10.2.min.js"><\/script>')</script>
    <script type=text/javascript  src="http://www.bungeer.com/static/js/video_html5.js"></script>



[1]: http://bungeer.com/app/android
[2]: http://www.videojs.com