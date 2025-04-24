from django.shortcuts import redirect, render

from produto.models import Produto


def cadastrar(request):
    
    if request.method == "GET":
        produtos = Produto.objects.all()

        soma = sum(obj.preco for obj in produtos)

        return render(request, "cadastrar.html", {"produtos": produtos, "soma": soma})
    elif request.method == "POST":
        nome = request.POST.get("inputProduto")
        preco = request.POST.get("inputPreco")

        produto = Produto(nome=nome, preco=preco)

        produto.save()

        return redirect("cadastrar")


def exluir(request, id):
    produto = Produto.objects.get(id=id)

    produto.delete()

    return redirect("cadastrar")
