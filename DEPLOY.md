# Permify Python Deployment

## Deploying Process

The release process is automated via GitHub Actions. Here’s how it works:

1. **Triggering the Generator Workflow**  
   - After a release is created in the `main` branch of main `Permify` repository, the generator workflow will be triggered automatically.  
   - If it does not trigger automatically, it can be run manually using **Workflow Dispatch**.  

2. **Pull Request Creation & Merge**  
   - The generator workflow will create a pull request and merge it back into the repository.  

3. **Release Creation**  
   - After the merge, the workflow will create a release with the **same version** as the generated code.  

4. **PyPI Deployment**  
   - Once the release is created, the package will be automatically deployed to **PyPI**.  
