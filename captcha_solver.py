from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

api_key = '4a27760ccb2a74b1860b6ff07dd00ab8'
site_key = '6LdUQnIUAAAAAM_pYgzYhqdgL3w6xH5SMty7XMhb'  # grab from site
# 6LdUQnIUAAAAAM_pYgzYhqdgL3w6xH5SMty7XMhb

url = 'https://www.komparify.com/users/sign_in'

client = AnticaptchaClient(api_key)
task = NoCaptchaTaskProxylessTask(url, site_key)
job = client.createTask(task)
job.join()
print(job.get_solution_response())

