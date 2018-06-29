$(document).ready(function () {
								function change() {
									var link = ($("#link").val() != "") ? $("#link").val() : "https://www.facebook.com/thietkeweb30s.org";
									var link1 = link.replace("https://www.facebook.com/", "");
									var height = parseInt($("#height").val());
									var width = parseInt($("#width").val());
									var width1 = width-2;
									var anhien = $("input[name='anhien']:checked").val();
									 var src = "https://www.facebook.com/v2.10/plugins/page.php?adapt_container_width=true&app_id=&channel=http%3A%2F%2Fstatic.ak.facebook.com%2Fconnect%2Fxd_arbiter%2FwjDNIDNrTQG.js%3Fversion%3D41%23cb%3Df3c840f1bb4b94%26domain%3Dlocalhost%26origin%3Dhttp%253A%252F%252Flocalhost%253A63342%252Ff2ca5fb6c60c61a%26relation%3Dparent.parent&container_width=400&height=200&hide_cover=false&href=https%3A%2F%2Fwww.facebook.com%2F" + link1 + "&locale=vi_VN&sdk=joey&show_facepile=true&show_posts=false&small_header=false&tabs=messages&width=" + width + "px&height=" + height + "px";
									$("#fbPreview").attr("src", (src));
									$("#fbPreview").css("height", height);
									var string2 =
											'<div id="fb-root"></div>' +
											'<script>' +
											'$(document).ready(function() {' +
											'var raido = $(".wrap").attr("data-toggle");' +
											'if(raido==1){' +
											'$(".vnk-tuvan").css("display","none");' +
											'$(".x").click(function(){' +
											'$(".wrap").slideToggle();$(".vnk-tuvan").slideToggle();' +
											'});' +
											'$(".vnk-tuvan").click(function(){' +
											'$(".wrap").slideToggle();$(this).slideToggle();' +
											'});' +
											' }else{' +
											'$(".wrap").css("display","none");' +
											'$(".x").click(function(){' +
											'$(".wrap").slideToggle();$(".vnk-tuvan").slideToggle();' +
											'});' +
											'$(".vnk-tuvan").click(function(){' +
											'$(".wrap").slideToggle();$(this).slideToggle();' +
											'});' +
											'}' +
											'})' +
											' (function(d, s, id) {' +
											'var js, fjs = d.getElementsByTagName(s)[0];' +
											'if (d.getElementById(id)) return;' +
											'js = d.createElement(s); js.id = id;' +
											'js.src = "//connect.facebook.net/vi_VN/sdk.js#xfbml=1&version=v2.10&&appId=126586364523772";' +
											'fjs.parentNode.insertBefore(js, fjs);' +
											'}(document, "script", "facebook-jssdk"));</script>' +
											'<style>.wrap{position:fixed; width:300px; height: 400px; z-index:9999999; right:0px; bottom:0px;}.x{font-family: arial, helvetica;background: rgba(78,86,101,0.8) none repeat scroll 0 0;font-size:14px;font-weight:bold;color: #fff;display: inline-block;height: 25px;line-height: 25px;position: absolute;right: 0;text-align: center;top: -19px;width: 25px;z-index: 99999999;}.x:hover{cursor: pointer;}.pxem{text-align:left;height:20px;margin-bottom: 0;margin-top: 0;background: #34495E;width:100%;bottom: 0;display: block;left: 0px;position: absolute;z-index: 999999999;border-left: 1px solid #fff;}.pxem a.axem{color: #fff;font-family: arial,helvetica;font-size: 12px;line-height: 23px;padding-left: 5px;text-decoration: none;}.pxem a.axem:hover{text-decoration: underline;}.alogo{position: absolute;bottom: 0;right: 0px;z-index: 999999999999;width: 75px;height: 20px;display: inline-block;background:#34495E;border-left:2px solid #2c3e50;padding-right: 0px;padding-left: 5px}.vnk-tuvan{position:fixed;width: 300px;background:#34495E;z-index:99999999;right:0px;bottom:0px;  border-style: solid solid none;border-width: 1px 1px 0; border-color: #2c3e50}.vnk-tuvan p{color: #fff;font-size: 15px;margin: 0;padding: 0 13px; text-align: left;}.vnk-tuvan p a{color: #fff;font-size: 15px;padding: 5px 0px 7px;margin: 0;display:inline-block;font-family: arial, helvetica;text-decoration: none;}.vnk-tuvan p a:hover{text-decoration: underline;cursor: pointer;}.vnk-tuvan p img {float: right;margin-top: 10px;} </style>' +
											'<div data-toggle="' + anhien + '" class="wrap" style="position:fixed; width:' + width + 'px; height: ' + height + 'px; ">' +
											'<span class="x" style="">X</span>' +
											'<div class="fb-page" data-adapt-container-width="true" data-height="' + height + '" data-hide-cover="false" data-href="' + link + '" data-show-facepile="true" data-show-posts="false" data-small-header="false" data-tabs="messages" data-width="' + width + '" style="position:relative; z-index:9999999; right:0px; bottom:21px;border-left: 1px solid #fff;border-top: 1px solid #fff;">' +
											'</div>' +
											'<p class="pxem" style="">' +
											'<a class="axem" style="" href="http://thietkeweb30s.org/" target="_blank">Tạo live chat facebook cho website</a>' +
											'<a class="alogo" style="">' +
											'<img src="http://thietkeweb30s.org/files/assets//logo_sam.png" width="60px" height="15px" style="margin-top: 3px"></a>' +
											'</p>' +
											'</div>' +
											'<div class="vnk-tuvan" style="width: ' + width1 + 'px;" >' +
											'<p style=" "><a style="">Bạn cần tư vấn ?</a><img src="https://image.prntscr.com/image/4X78J2NSTd2w1UrRr47ggA.png"></p>' +
											'</div>';

									$("#textarea").html(string2);

								}

								$("input[name='anhien']:checked").change(function () {
									change();
								})
								$("#width").change(function () {
									change();
								})
								$("#height").change(function () {
									change();
								})
								$("#link").change(function () {
									change();
								});
								$("#creatcode").click(function () {
									change();
								})
							})
