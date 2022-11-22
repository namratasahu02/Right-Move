from django.shortcuts import redirect, render
from django.views import View
from vendor.models import Product, Bullet_point, Image
from configuration.models import Category, Status_type, Size_unit, Image_type, State
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Edit_product(LoginRequiredMixin, View):
    def get(self, request, pid):
        context = {}
        p =  Product.objects.all().filter(id=pid, owner=request.user).first()
        images = Image.objects.all().filter(product=p)
        bps = Bullet_point.objects.all().filter(product=p)
        
        if p:
            context.update({
                'page_name' : 'Edit Product',
                'category' : p.category,
                'status' : p.status,
                'title' : p.title,
                'price' : p.price,
                'mrp' : p.mrp,
                'brand' : p.brand,
                'size' : p.size,
                'size_unit' : p.size_unit,
                'description' : p.description,
                'img_types' : Image_type.objects.all(),
                'state' : p.state,
                'district' : p.district,
                'zip_code' : p.zip_code,
                'address' : p.address,

                'images' : images,
                'bps' : bps,

                'states' : State.objects.all(),
                'categories' : Category.objects.all(),
                'all_status' : Status_type.objects.all(),
                'all_size_unit' : Size_unit.objects.all(),
            })

            return render(request, 'edit_product.html', context)

        else:
            messages(request, 'Product not found')

        return redirect('edit')

    def post(self, request, pid):
        product = Product.objects.all().filter(owner=request.user, id=pid).first()

        if product:
            if 'details' in request.POST:
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
                # Verify values
                category = Category.objects.all().filter(name=category)
                status = Status_type.objects.all().filter(name=status)
                size_unit = Size_unit.objects.all().filter(unit_name=size_unit)

                if product:
                    if category and status and title and mrp and price and size and size_unit:
                        product.owner = request.user 
                        product.category = category[0]
                        product.status = status[0]
                        product.title = title
                        product.mrp = mrp
                        product.price = price
                        product.brand = brand
                        product.size = size
                        product.size_unit = size_unit[0]
                        product.state = state
                        product.district = district
                        product.address = address
                        product.zip_code = zip_code
                        product.description =  description
                        product.save()
                        messages.success(request, 'Details successfully updated')

                    else:
                        messages.error(request, 'Required fields has no data.')
                        return redirect('edit', pid)

                else:
                    messages.error(request, 'Item not found.')
                    return redirect('dashboard')

            elif 'add_images' in request.POST:
                for i in range(1, 10):
                    img = request.FILES.get(f'image-{i}')
                    if img:
                        img_type = request.POST.get(f'img-type-{i}')
                        img_type = Image_type.objects.all().filter(type_name=img_type)

                        if img_type:
                            Image(product=product, image=img, image_type=img_type[0]).save()
                        else:
                            Image(product=product, image=img).save()
                    else:
                        break;
                
                messages.success(request, 'Image successfully added.')

            elif 'remove_image' in request.POST:
                image_id = request.POST.get('image_id')
                Image.objects.all().filter(id=image_id, product=product).delete()

            elif 'bullet_points' in request.POST:
                Bullet_point.objects.all().filter(product=product).delete()
                
                # Save Product bullet point
                for i in range(1, 10):
                    bp = request.POST.get(f'bullet-point-{i}')
                    if bp:
                        Bullet_point(product=product, bullet_point=bp).save()

                    else:
                        break;

        else:
            return messages.error(request, 'Something went wrong.')
        return redirect('edit', pid)

    # ==============