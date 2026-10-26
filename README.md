# Local GitOps sample (kind + Argo CD)

```
my-app/              # manifests Argo CD syncs (stand-in for Appernetes output)
argocd/application.yaml   # tells Argo CD what to watch
```

## Use it
1. Push this folder to a personal GitHub/GitLab.com repo (not Glass Lewis ADO).
2. Edit `repoURL` in `argocd/application.yaml`.
3. `kubectl apply -f argocd/application.yaml`
4. Watch it sync: `kubectl -n my-app get pods` (or the UI at https://localhost:8080 after
   `kubectl port-forward svc/argocd-server -n argocd 8080:443`).
5. Try the GitOps loop: change `replicas` in `my-app/deployment.yaml`, commit, push, and watch Argo CD scale it. Don't use kubectl for the change.
6. Reach the app: `kubectl -n my-app port-forward svc/my-app 8081:80`, then http://localhost:8081

Tear down: `kind delete cluster --name runtime-lab`
