from django.views import View
from django.shortcuts import redirect, render
from configuration.models import Category, Status_type, Size_unit, Image_type, State
from vendor.models import Product, Image, Bullet_point
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Add_product(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'page_name' : 'List new Property',
            'categories' : Category.objects.all(),
            'all_status' : Status_type.objects.all(),
            'all_size_unit' : Size_unit.objects.all(),
            'img_types' : Image_type.objects.all(),
            'states' : State.objects.all(),
        }
        return render(request, 'add_product.html', context)

    def post(self, request):
        # Get Form data
        category = request.POST.get('category')
        status = request.POST.get('status')
        title = request.POST.get('title')
        mrp = request.POST.get('mrp')
        price = request.POST.get('price')
        brand = request.POST.get('brand')
        size = request.POST.get('size')
        size_unit = request.POST.get('size_unit')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        description = request.POST.get('description')
        # Get forgin key values
        owner = request.user
        category = Category.objects.all().filter(name=category)
        status = Status_type.objects.all().filter(name=status)
        size_unit = Size_unit.objects.all().filter(unit_name=size_unit)

        if category and status and title and mrp and price and size and size_unit:
            # Save product model data
            product = Product(
                owner = owner, 
                category = category[0],
                status = status[0],
                title = title,
                mrp = mrp,
                price = price,
                brand = brand,
                size = size,
                size_unit = size_unit[0],
                state = state,
                district = district,
                address = address,
                zip_code = zip_code,
                description =  description,
            ).save()

            if product:
                # Save product images
                for i in range(1, 20):
                    img = request.FILES.get(f'image-{i}')
                    img_type = request.POST.get(f'img-type-{i}')
                    img_type = Image_type.objects.all().filter(type_name=img_type)
                    if img:
                        if img_type:
                            Image(product=product, image=img, image_type=img_type[0]).save()
                        else:
                            Image(product=product, image=img).save()
                    else:
                        break;

                # Save Product bullet point
                for i in range(1, 20):
                    bp = request.POST.get(f'bullet-point-{i}')
                    if bp:
                        Bullet_point(product=product, bullet_point=bp).save()

                    else:
                        break;

                return redirect('dashboard')

            else:
                messages.error(request, 'Something went wrong. Please contact us.')

        else:
            messages.error(request, 'Required fields has no data.')


        return redirect('add')




        
                












        





        for i in range(1, counter1):
            image = 'image-'+str(i)
            image = request.FILES.get(image)
            if image:
                images.update({
                    'image-'+str(i) : image, 
                })
            else:
                break;
        
        for i in range(1, counter2):
            bp = 'bullet-point-'+str(i)
            bp = request.POST.get(bp)
            if bp:
                points.update({
                    'bp-'+str(i) : bp,
                })
            else:
                break;

        print(f'''cat = {category} \n status = {status} \n title = {title} \n mrp = {mrp} \n price = {price} \n
                brand = {brand} \n qty = {qty} \n description = {description}\n {points} \n {images}''')

        return render(request, 'add_product.html', context)