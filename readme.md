# theblog - Project  
---------------------

## Models   

  ##  
    - Post
      - title  
      - slug  
      - content  
      - thumbnail  
      - category(ForeighKey = Category)  
      - tags(ManyToMany = Tag)  
  
  ##
    - Category
      - name  

  ##
    - Tag
      - name  
      - posts(ManyToMany = Post)
    
  ##  
    - User
      - full_name   
      - email   
      - password  
      - role  
      - profil  
  
  ##  
    - Like
      - post (Foreign = Post)  
      - user (Foreign = User)   
      - nb_like  
  
  ##  
    - Comment
      - content   
      - user (OneToOne = User)  
      - post (ForeighKey = Post)

## Fonctionnalités  
[x] Affichage posts  
[x] Affichage des posts populaires  
[x] Trie des posts par recherche, category et tags  
[x] Authentication User  
[] Mise à jour profil  
[] Enregistrement User  
[] Envoi mail de réinitialisation de mot de passe  
[] Attribution de rôle  
[x] Commenter un post   
[] Répondre à un commentaire  
[x] Aimer un post  
[] Création post   
[] Suppression post  
[] Mise à jour post  
[x] Associer des tags et une category à un post   