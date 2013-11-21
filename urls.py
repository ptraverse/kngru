from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',            
	url(r'^create-post','gim3.gimmeapp.views.create_post'),
	url(r'^new-post','gim3.gimmeapp.views.new_post_form'),
	url(r'^allposts','gim3.gimmeapp.views.view_all_posts'),
				
	url(r'^post/(.*)','gim3.gimmeapp.views.view_post'),
	url(r'^url-redirect/(.*)','gim3.gimmeapp.views.url_redirect'), 
	 
	url(r'^sign-up','gim3.gimmeapp.views.sign_up'),
	url(r'^log-in','gim3.gimmeapp.views.log_in'),
    url(r'^log-out','gim3.gimmeapp.views.log_out'),
    
    url(r'^user/(.*)/friends','gim3.gimmeapp.views.user_friends'),
    url(r'^user/(.*)/receipts','gim3.gimmeapp.views.user_receipts'),
    url(r'^user/(.*)/edit','gim3.gimmeapp.views.user_edit'),
    url(r'^user/(.*)','gim3.gimmeapp.views.user_home'),
    
    url(r'^target','gim3.gimmeapp.views.target'),
    url(r'^create-target','gim3.gimmeapp.views.create_target'),
    
    url(r'','gim3.gimmeapp.views.landing_page'),
    url(r'^(.+)','gim3.gimmeapp.views.e404_page'),
    
	
    # url(r'^preform','gim3.gimmeapp.views.preform'),
    # url(r'^hello_world/(.*)','gim3.gimmeapp.views.hello_world'),
	
    # Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^/admin/doc/', include('django.contrib.admindocs.urls')),
    
    
)
